import requests, json

url = 'https://sandbox.techops.engineering/Demand/v1/Surveys/BySurveyNumber/4592039'
params = ""
headers = {'Content-type': 'application/json', 'Authorization' : 'YOUR_API_KEY_HERE', 'Accept': 'text/plain'}
response = requests.get(url, data=params, headers=headers)
print(response.content.decode())

file = open("survey_get.json","w")
file.write(response.text)
file.close()

