# This is a sample Python script.
import requests
import json
mac_address = input("Enter you mac address:")
url = "https://api.macaddress.io/v1?apiKey=at_cXLD3nVupldPOnSjojjgnqlVlazpe&output=json&search="
url=url+mac_address

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data = payload)

output = json.loads(response.text.encode('utf8'))

print(mac_address, output["vendorDetails"]["companyName"])


