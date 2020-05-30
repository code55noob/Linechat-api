import requests
 
url = 'https://notify-api.line.me/api/notify'

token = 'your token'

headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}
 
msg = 'ฉันเป็น bot'

r = requests.post(url, headers=headers , data = {'message':msg})

print(r.text)