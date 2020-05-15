import settings
import json
import os
import time

response_key = os.getenv("RESPONSE_KEY")
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
refresh_token = os.getenv("REFRESH_TOKEN")
organizer_key = os.getenv("ORGANIZER_KEY")
webinar_key = os.getenv("WEBINAR_KEY")


import requests
import base64

consumer_b64 = base64.b64encode("{}:{}".format(consumer_key, consumer_secret).encode())
base_url = "https://api.getgo.com/G2W/rest/v2"


# source: https://goto-developer.logmeininc.com/how-get-access-token-and-organizer-key
# can only be used once per access token acquired -- so call this sparingly
def post_access_token():
    url = "https://api.getgo.com/oauth/v2/token"
    headers = {
        "Authorization": "Basic {}".format(consumer_b64.decode()),
        "Accept": "Application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        # this may be able to broken up, not sure right now
        "grant_type": "authorization_code",
        "code": response_key
    }
    r = requests.post(url, data=data, headers=headers).json()
    # at this point, just copy and past the tokens from the terminal into the .env
    print(r)

    return r
    

def post_refresh_token():
    url = "https://api.getgo.com/oauth/v2/token"
    headers = {
        "Authorization": "Basic {}".format(consumer_b64.decode()),
        "Accept": "Application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        # this may be able to broken up, not sure right now
        "grant_type": "refresh_token",
        "refresh_token": refresh_token
    }
    r = requests.post(url, data=data, headers=headers).json()
    # at this point, just copy and past the tokens from the terminal into the .env
    print(r)
    print("**********************")
    print("Remember to replaced REFRESH_TOKEN & ACCESS_TOKEN into your .env before the next run (sorry)")

    return r

def create_registrant_v1(registrants):
    url = "https://api.getgo.com/G2W/rest/v2/organizers/{}/webinars/{}/registrants?resendConfirmation=false".format(organizer_key, webinar_key)
    headers = {
        "Authorization": "Bearer {}".format(access_token),
        "Accept": "Application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    # data = {
    #     "firstName": "David",
    #     "lastName": "S",
    #     "email": "dsilv022@ucr.edu"
    # }
    responses = []
    for registrant in registrants:
        time.sleep(1); 
        responses.append({ **requests.post(url, data=json.dumps(registrant), headers=headers).json(), **registrant })
    headers = ["registrantKey", "joinUrl", "status", "description", "asset", "firstName", "lastName", "email"]
    # print(r)
    return (responses, headers)

def get_webinars():
    start = '2020-05-11T00:00:00Z'
    end = '2020-05-15T00:00:00Z'
    url = "{}/organizers/{}/webinars?fromTime={}&toTime={}".format(base_url, organizer_key, start, end)
    headers = {
        "Authorization": "Bearer {}".format(access_token),
        "Accept": "Application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    r = requests.get(url,headers=headers).json()
    # at this point, just copy and past the tokens from the terminal into the .env
    print(r)

# TODO: create webinar, get webinars, select webinar, then create registrants

# post_access_token()
# post_refresh_token()
# get_webinars()
# create_registrant_v1()