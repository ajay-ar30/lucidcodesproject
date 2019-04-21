import requests, json
url = 'https://sandbox.techops.engineering/Demand/v1/Surveys/Update/4592039'

params= {
        "AccountID": 430,
        "UniqueIPAddress": True,
        "ClientSurveyLiveURL": "https://www.surveyURL.com?rid=[%RID%]",
        "BidLengthOfInterview": 10,
        "IsVerifyCallBack": False,
        "QuotaCalculationTypeID": 1,
        "QuotaCPI": 0.80,
        "FulcrumExchangeAllocation": 0,
        "BusinessUnitID": 125,
        "FulcrumExchangeHedgeAccess": True,
        "SampleTypeID": 100,
        "IsRelevantID": False,
        "IsDedupe": False,
        "FraudProfileThreshold": 0,
        "UniquePID": True,
        "Quota": 5,
        "IsTrueSample": False,
        "ClientCPI": 1.20,
        "CollectsPII": None,
        "IsGeoIP": False,
        "StudyTypeID": 1,
        "IndustryID": 30,
        "SurveyPlatformID": 1,
        "CountryLanguageID": 9,
        "AccountID": 430,
        "SurveyStatusCode": "01",
        "SurveyPriority": 11,
        "SurveyNumber": 4592039,
        "IsFraudProfile": False,
        "IsActive": True,
        "BidIncidence": 20,
        "SurveySID": "90faa10f-8944-4e02-a360-0ae22a413fd2",
        "SurveyName": "Example API Survey",
        "TestRedirectURL": "https://www.surveyURL.com?rid=[%RID%]"
    }

data = json.dumps(params) #dumps is serializing 'params' object to a JSON formatted string and storing in data object
headers = {'Content-type': 'application/json', 'Authorization' : 'YOUR_API_KEY_HERE', 'Accept': 'text/plain'}
response = requests.put(url, data=data, headers=headers)
print(response.content.decode())

file = open("survey_update.json","w")
file.write(response.text)
file.close()