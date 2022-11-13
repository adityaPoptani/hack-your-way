import json
import requests
import re

class VoterID:
    def __init__(self, serial_num, full_name, wco_name, house_number, age_and_gender, epic_num):
        self.serial_num=serial_num
        self.full_name=full_name
        self.last_name=full_name.split()[-1]
        self.house_number=house_number
        self.wco_name=wco_name
        self.age=re.findall(r'\d+', age_and_gender)
        self.epic_num=epic_num
        self.age_and_gender=age_and_gender


def get_captcha_from_google_api(image):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    data = {
    "requests": [
        {
        "image": {
            "content": image
        },
        "features": [
            {
            "type": "TEXT_DETECTION"
            }
        ]
        }
    ]
    }

    post_request=requests.post("https://vision.googleapis.com/v1/images:annotate?key=AIzaSyBT6liLYumaZlMnb5uQnxKlFkkwsCDui10", json=data, headers=headers)
    post_request=post_request.content.decode()
    post_request=json.loads(post_request)
    print(post_request)
    response=post_request['responses'][0]['textAnnotations'][0]['description']
    res_list = (response.split('\n'))
    return res_list[0]

def parser(image):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    data = {
    "requests": [
        {
        "image": {
            "content": image
        },
        "features": [
            {
            "type": "TEXT_DETECTION"
            }
        ]
        }
    ]
    }
    post_request=requests.post("https://vision.googleapis.com/v1/images:annotate?key=AIzaSyBT6liLYumaZlMnb5uQnxKlFkkwsCDui10", json=data, headers=headers)
    post_request=post_request.content.decode()
    post_request=json.loads(post_request)

    response=post_request['responses'][0]['textAnnotations'][0]['description']
    language=post_request['responses'][0]['textAnnotations'][0]['locale']

    res_list = (response.split('\n'))

    try:
      serial_num=res_list[0]
    except Exception as e:
      serial_num=""

    try:
      full_name=res_list[1]
    except Exception as e:
      full_name=""

    last_name=full_name.split()[-1]

    try:
      wco_name=res_list[2]
    except Exception as e:
      wco_name=""
    
    try:
      house_number=res_list[3]
    except Exception as e:
      house_number=""

    try:
      age_and_gender=res_list[4]
    except Exception as e:
      age_and_gender=""

    try:
      epic_num=res_list[5]
    except Exception as e:
      epic_num=""
    
    voter=VoterID(serial_num,full_name,wco_name,house_number,age_and_gender,epic_num)

    # return {
    #   "epic_number": epic_num,
    #   "full_name": full_name,
    #   "last_name": last_name,
    #   "wco_name": wco_name,
    #   "house_number": house_number,
    #   "age": voter.age,
    #   "age_and_gender": voter.age_and_gender
    # }

    return voter


def findFamily(voterID, data):

    familyMembers=[]
    houseNum=None
    for voter in data:
        if(voter.epic_num==voterID):
            houseNum=voter.house_number
            break

    for potentialMember in data:
        if(potentialMember.epic_num!=voterID and potentialMember.house_number==houseNum):
            familyMembers.append(potentialMember)

    return familyMembers
