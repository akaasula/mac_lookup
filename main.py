
import requests
import json
import re
mac_address = input('Please enter a MAC address, (Example xx:xx:xx:xx:xx:xx )\n')
while mac_address!=None:
    valid = re.match('(?=[a-f0-9]{2}:){5}[a-f0-9]{2}', mac_address, re.I)
    url = "https://api.macaddress.io/v1?apiKey=at_cXLD3nVupldPOnSjojjgnqlVlazpe&output=json&search="
    url = url + mac_address
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    output = json.loads(response.text.encode('utf8'))
    if output["vendorDetails"]["companyName"]=="":
        print("Invalid mac address or doesnt belongs to any vendor")
    else:
        print('This mac address, {} belongs to: \n '.format(mac_address) + output["vendorDetails"]["companyName"])
        break
    try:
        response = requests.get(url, headers=headers, data=payload, timeout=4)
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        print("Http Error!, Status code: ", response.status_code)
        break
        




