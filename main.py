import requests
from _datetime import datetime
import os

USERNAME = os.environ.get("USERNAME")
pixela_endpoint = os.environ.get("pixela_endpoint")
TOKEN = os.environ.get("TOKEN")
GRAPH_ID = os.environ.get("GRAPH_ID")

user_params = {
	"token": TOKEN,
	"username": USERNAME,
	"agreeTermsOfService": "yes",
	"notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json= user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
	"id": GRAPH_ID,
	"name": "Cycling Graph",
	"unit": "Km",
	"type": "float",
	"color": "ajisai"
}

headers = {
	"X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json= graph_params, headers = headers)
# print(response.text)

pixela_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

value_params = {
	"date": today.strftime("%Y%m%d"),
	"quantity": input("How many kilometers did you cycle today? "),
}

response = requests.post(url=pixela_graph_endpoint, json= value_params, headers = headers)
print(response.text)


# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
#
# new_pixel_data = {
# 	"quantity": "4.5",
# }
#
# response = requests.put(url = update_endpoint, json= new_pixel_data, headers = headers)
#
# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
#
# requests.delete(url=delete_endpoint, headers= headers)
# print(response.text)