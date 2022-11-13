from django.shortcuts import render
from django.conf import settings
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium import webdriver

import requests
import json
import os

from main.utils import *
from main.good_states import download
from main.utils_pdf import PDFClass
from main.parseCards import parser, findFamily, get_captcha_from_google_api
from main.family_making_algo import get_family_relations

def pdf_processing(pdf_path):
	pdf_processor = PDFClass(pdf_path)
	pdf_processor.proc_pdf()
	pdf_processor.proc_all()

def attempts_to_get_voter_data(epic_number):
	success = False
	tries = 0
	while not success and tries < 10:
		tries += 1
		image_string = open_query_page_in_browser(epic_number)

		# res = requests.post(
		# 	url = "https://t5jerehghf5mqrpxyxtfhckzci0pyolc.lambda-url.us-east-1.on.aws/",
		# 	json = {
		# 		"Image": str(image_string)
		# 	}
		# )

		# captcha = str(res.text)

		captcha = get_captcha_from_google_api(image_string)
		captcha = captcha.replace("\n", '')
		print(captcha)

		voter_data = json.loads(entercaptcha(captcha))
		if voter_data["status"] == "success":
			success = True
			print(voter_data)
			return voter_data
		else:
			print("Wrong captcha")
	return 0

def get_selected_cards_for_family_scanning(sr_no):
	sr_no = int(sr_no)
	cards_dir = str(settings.BASE_DIR) + "/cards"
	sorted_files = sorted(os.listdir(cards_dir))

	suitable_for_scanning = []

	HALF_RANGE = 20
	me_ind = sr_no - 1
	if me_ind >= 0 and me_ind < len(sorted_files):
		i = 1
		while i <= HALF_RANGE and (me_ind - i >= 0):
			suitable_for_scanning.append(sorted_files[me_ind - i])
			i += 1
		
		i = 1
		while i <= HALF_RANGE and (me_ind + i < len(sorted_files)):
			suitable_for_scanning.append(sorted_files[me_ind + i])
			i += 1

		return suitable_for_scanning
	else:
		return []


class PrimaryQueryView(APIView):
	def post(self, request):
		data = request.data
		print(data)

		epic_number = data["epic_number"]
		
		voter_data = attempts_to_get_voter_data(epic_number)
		if voter_data == 0:
			return Response({
				"persons": []
			}, status.HTTP_200_OK)
		
		voter_info = voter_data["data"]
		pdf_util_info = parse_id_for_voter(voter_info["id"])
		
		required_pdf_url = url_generation_for_pdf(
			voter_info["State"],
			voter_info["District"],
			str(pdf_util_info["ac_no"]),
			str(pdf_util_info["part_no"]),
			str(pdf_util_info["sr_no"])
		)
		print(required_pdf_url)
		pdf_path = download(required_pdf_url)
		pdf_processing(pdf_path)

		cards_for_family_scanning = get_selected_cards_for_family_scanning(voter_info["Serial_No"])
		if len(cards_for_family_scanning) == 0:
			return Response({
				"persons": []
			}, status.HTTP_200_OK)
		print(cards_for_family_scanning)
		
		all_cards_data = []
		cards_dir = str(settings.BASE_DIR) + "/cards"
		for file in os.listdir(cards_dir):
			img_name = cards_dir + "/" + str(file)

			print(img_name)
			with open(img_name, "rb") as img_file:
				img = img_file.read()
				img_string = base64.encodebytes(img).decode('utf-8')
				voter_of_card = parser(img_string)

				all_cards_data.append(voter_of_card)
			os.remove(img_name)

		family_members = findFamily(epic_number, all_cards_data)
		print(family_members)

		epics_of_family = []
		for member in family_members:
			epics_of_family.append(member.epic_num)

		members = []
		for epic in epics_of_family:
			member_data = attempts_to_get_voter_data(epic)

			if member_data is not 0:
				member_info = member_data["data"]
				# members.append({
				# 	"name": member_info["Name"],
				# 	"relation": "Relative"
				# })
				members.append({
					"name" : member_info["Name"],
					"age" : int(member_info["Age"]),
					"gender" : member_info["Gender"],
					"mid_name" : member_info["Father's/Husband's_Name"],
					"epic" : epic
				})
		my_data = {
			"name" : voter_info["Name"],
			"age" : int(voter_info["Age"]),
			"gender" : voter_info["Gender"],
			"mid_name" : voter_info["Father's/Husband's_Name"],
			"epic" : epic_number
		}
		relations = get_family_relations(my_data, members)

		final_output = []
		for relation in relations:
			final_output.append({
				"name": relation[0],
				"relations": relation[1]
			})

		return Response({
			"persons": final_output
		}, status = status.HTTP_200_OK)
