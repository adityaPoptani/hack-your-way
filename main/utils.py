import time
import sys
import base64
import json

from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
from pytesseract import *

from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium import webdriver

from pdf2image import convert_from_path

from main.good_states import STATE_FUNCTIONS

GOOD_STATES = [
	"Assam",
	"Gujarat",
	"West Bengal",
	"Goa",
	"Chandigarh",
	"Sikkim",
	"Mizoram",
	"Meghalaya",
	"Lakshwadeep",
	"Delhi"
]

GOOD_STATES_WITH_CAPTCHA = [
	"Telangana",
	"Andhra Pradesh",
	"Karnataka",
]

NON_FUNCTIONAL_STATES = [
	"Nagaland",
	"Odisha",
	"Tamil Nadu",
	"Uttarakhand",
	"Arunachal Pradesh",
	"Kerala",
]

LESS_PDF_STATES = [
	"Manipur"
]


WIDTH = 401
HEIGHT = 158
SR_NO_RIGHT_X = 5

def crop_image(img_name, size, location):
	img = Image.open(img_name) # uses PIL library to open image in memory

	left = location['x']
	top = location['y']
	right = location['x'] + size['width']
	bottom = location['y'] + size['height']

	img = img.crop((left, top, right, bottom)) # defines crop points
	img.save(img_name)

def open_query_page_in_browser(epic_number):
	global driver
	try:
		options = Options()
		#options.headless = True
		options.add_argument("--no-sandbox")
		options.add_argument("--headless")
		options.add_argument("--disable-gpu")
		options.add_argument('--user-agent="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166"')

		driver = webdriver.Chrome(options=options)
		driver.get('https://electoralsearch.in/')
		driver.set_window_size(1120, 850)
		
		try:
			welcome_button = driver.find_elements("xpath", "//*[@id='welcomeDialog']/div/div/div/input")[0]
			welcome_button.click()
		except:
			pass
		search_by_epic_number = driver.find_elements("xpath", "//*[@role='tablist']/li[2]")[0]
		search_by_epic_number.click()

		time.sleep(3)

		text = driver.find_element("id", 'name')
		text.send_keys(epic_number)

		element = driver.find_element("id", 'captchaEpicImg')
		location = element.location
		size = element.size
		img_name = epic_number.replace("/", "_")+'.png'
		driver.save_screenshot(img_name)

		crop_image(img_name, size, location)

		with open(img_name, "rb") as img_file:
			img = img_file.read()
			img_string = base64.encodebytes(img).decode('utf-8')
			
			return img_string		

	except Exception as e:
		print("Error: " + str(e))
		driver.quit()

def entercaptcha(captcha_text):
	global driver
	try:
		text = driver.find_element("id", 'txtEpicCaptcha')
		text.send_keys(captcha_text)

		# click on submit button
		epic_submit = driver.find_element("id", 'btnEpicSubmit')
		epic_submit.click()
		time.sleep(3)

		# fetch all epic data
		epic_data = driver.find_elements("xpath", "//*[@id='resultsTable']/tbody/tr/td/form/input[@type='hidden']")

		a, data = {}, {}	

		for i in epic_data:
			k = i.get_attribute('name')
			v = i.get_attribute('value')
			a[k] = v

		try:
			data["id"] = a["id"]
			data["epic_no"] = a["epic_no"]
			data["Name"] = a["name"]
			data["Gender"] = a["gender"]
			data["Age"] = a["age"]
			data["Father's/Husband's_Name"] = a["rln_name"]
			data["District"] = a["district"]
			data["State"] = a["state"]
			data["Serial_No"] = a["slno_inpart"]
		except Exception as e:
			print("Error 1: "+str(e))

			# finally convert all information to json
			return json.dumps({
				"status": "error", 
				"message": "Wrong captcha", 
				"data": data
			})

		return json.dumps({
			"status": "success", 
			"message": "Data extracted", 
			"data": data
		})

	except Exception as e:
		print("Error 2: "+str(e))
		return json.dumps({
			"status": "error", 
			"message": "Couldn't get data", 
			"data": data
		})

def parse_id_for_voter(id):
	id = str(id)
	return {
		"state_no": id[0:3],
		"ac_no": int(id[3:6]),
		"part_no": int(id[6:10]),
		"sr_no": int(id[12:16])
	}

def url_generation_for_pdf(state, district, ac_no, part_no, sr_no):
	if state in NON_FUNCTIONAL_STATES:
		return {
			"status": "error",
			"url": None
		}
	elif state in GOOD_STATES_WITH_CAPTCHA:
		pass
	elif state in GOOD_STATES:
		return STATE_FUNCTIONS[state](district, ac_no, part_no, sr_no)
