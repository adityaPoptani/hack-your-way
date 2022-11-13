import time
import os

from django.conf import settings

from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium import webdriver

from main.constants import STATE_INFO as info

def generate_url_assam(district, ac_no, part_no, sr_no):
    state_info = info["Assam"]

    base_url = state_info["modifiable_website_root"]

    dist_no = state_info["district_map"][district.upper()]

    suffix = state_info["suffix_formatted_string"].format(dist_no = dist_no, ac_no = ac_no, part_no = part_no)

    final_url = base_url + suffix
    
    return final_url

def generate_url_goa(district, ac_no, part_no, sr_no):
    state_info = info["Goa"]

    base_url = state_info["modifiable_website_root"]

    suffix = state_info["suffix_formatted_string"].format(ac_no = ac_no, part_no = part_no)

    final_url = base_url + suffix
    
    return final_url

def generate_url_gujarat(district, ac_no, part_no, sr_no):
    state_info = info["Gujarat"]

    base_url = state_info["modifiable_website_root"]

    suffix = state_info["suffix_formatted_string"].format(int(ac_no), ac_no = ac_no, part_no = part_no)

    final_url = base_url + suffix
    
    return final_url

def generate_url_west_bengal(district, ac_no, part_no, sr_no):
    state_info = info["West Bengal"]

    base_url = state_info["modifiable_website_root"]

    dist_no = state_info["district_map"][district.upper()]

    suffix = state_info["suffix_formatted_string"].format(dist_no = dist_no, ac_no = ac_no, part_no = part_no)

    final_url = base_url + suffix
    
    return final_url

def generate_url_chandigarh(district, ac_no, part_no, sr_no):
    state_info = info["Chandigarh"]

    base_url = state_info["modifiable_website_root"]

    suffix = state_info["suffix_formatted_string"].format(int(ac_no))

    final_url = base_url + suffix
    return final_url

def generate_url_sikkim(district, ac_no, part_no, sr_no):
    state_info = info["Sikkim"]

    base_url = state_info["modifiable_website_root"]

    suffix = state_info["suffix_formatted_string"].format(part_no = part_no)

    final_url = base_url + suffix
    return final_url

def generate_url_mizoram(district, ac_no, part_no, sr_no):
    state_info = info["Mizoram"]

    base_url = state_info["modifiable_website_root"]

    suffix = state_info["suffix_formatted_string"].format(ac_no = ac_no, part_no = part_no)

    final_url = base_url + suffix
    return final_url

def generate_url_meghalaya(district, ac_no, part_no, sr_no):
    state_info = info["Meghalaya"]

    base_url = state_info["modifiable_website_root"]

    suffix = state_info["suffix_formatted_string"].format(int(ac_no), int(ac_no), int(part_no))

    final_url = base_url + suffix
    return final_url

def generate_url_lakshwadweep(district, ac_no, part_no, sr_no):
    state_info = info["Lakshwadweep"]

    base_url = state_info["modifiable_website_root"]

    suffix = state_info["suffix_formatted_string"].format(ac_no=ac_no, part_no=part_no)

    final_url = base_url + suffix
    return final_url

def generate_url_delhi(district, ac_no, part_no, sr_no):
    state_info = info["Delhi"]

    base_url = state_info["modifiable_website_root"]

    suffix = state_info["suffix_formatted_string"].format(ac_no=ac_no, part_no=part_no)

    final_url = base_url + suffix
    return final_url


def latest_download_file():
    downloads_folder = "downloads/"
    os.chdir(downloads_folder)
    files_sorted_by_time = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
    latest_file = files_sorted_by_time[-1]
    os.chdir("..")
    return latest_file

def download(url):
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_experimental_option('prefs', {
        "download.default_directory": "downloads/", 
        "download.prompt_for_download": False, 
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True 
    })
    driver = webdriver.Chrome(options=options)
    
    driver.get(url)
    time.sleep(5)
    # TODO : rename the downloaded file
    print(url)

    path = str(settings.BASE_DIR) + "/downloads/" + latest_download_file()
    print(path)
    return path

STATE_FUNCTIONS = {
    "Assam": generate_url_assam,
    "Goa": generate_url_goa,
    "Gujarat": generate_url_gujarat,
    "West Bengal": generate_url_west_bengal,
    "Chandigarh": generate_url_chandigarh,
    "Sikkim": generate_url_sikkim,
    "Mizoram": generate_url_mizoram,
    "Meghalaya": generate_url_meghalaya,
    "Lakshwadweep": generate_url_lakshwadweep,
    "Delhi": generate_url_delhi
}