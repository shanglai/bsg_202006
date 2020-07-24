import requests
import json

data= 'Hola Flume'
url_flume = 'http://162.243.0.177:9260'
payload = [{'headers': {}, 'body': data }]
headers = {'content-type': 'application/json'}
response = requests.post(url_flume, data=json.dumps(payload),headers=headers)
