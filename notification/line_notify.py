from dotenv import load_dotenv
import requests, json, time, os

def send(token, cases) -> None:
    headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    for case in cases:
        payload = {'message': case }
        r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
