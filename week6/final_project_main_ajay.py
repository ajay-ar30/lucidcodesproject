# Import necessary packages
import requests
import json
import csv

# Define API key for use in multiple API calls
API_KEY = ''

# Create empty list to which results can be appended
finalCsvData = []

# Let the user know the script is starting
print('Starting...')

# Create output file header list 
outputCsvHeader = ["SurveyNumber", "SurveyName","SurveyStatusCode", "CountryLanguageID", "QuotaCPI","BidLengthOfInterview", 
"Quota", "Prescreens", "Completes", "TotalQuotaRemaining", "IsVerifyCallBack"]

# Append output header to final list
finalCsvData.append(outputCsvHeader)

# Open the input CSV file
with open('input.csv') as csvfile:
    # Read data from file in dictionary form using DictReader            
    reader = csv.DictReader(csvfile)

    # Loop through every row in the CSV file
    for row in reader:
        print(row)
        # Accessing and storing surveynumbers from SurveyNumber column in file to surveyNumber variable
        surveyNumber = row['ï»¿SurveyNumber']
        # Prod URL for surveys as only GET requests used
        surveyDetailsUrl = "https://api.samplicio.us/Demand/v1/Surveys/BySurveyNumber/{}".format(surveyNumber)
        headers = {'Content-type': 'application/json','Authorization': API_KEY, 'Accept': 'text/plain'}
        # Make the GET call to the Marketplace
        surveyDetailsJson = requests.get(url=surveyDetailsUrl, headers=headers)
        # Load the JSON string received from the API as a Python dictionary
        surveyDetailsJson = json.loads(surveyDetailsJson.content.decode())
        # Accessing and storing the 'Survey' dictionary from the API response in SurveyDetails variable
        SurveyDetails = surveyDetailsJson['Survey'] 
        surveyQuotaUrl = "https://api.samplicio.us/Demand/v1/SurveyQuotas/BySurveyNumber/{}".format(surveyNumber)
        headers = {'Content-type': 'application/json','Authorization': API_KEY, 'Accept': 'text/plain'}
        surveyQuotaJson = requests.get(url=surveyQuotaUrl, headers=headers)
        surveyQuotaJson = json.loads(surveyQuotaJson.content.decode())
        SurveyQuota = surveyQuotaJson['Quotas']
        #Loop through SurveyQuota 
        for quota in SurveyQuota:
            if quota["Name"] == "Total":
                SurveyQuota = quota
                break
           # Print QuotaCalculationTypeID values for the surveys
        print("QuotaCalculationTypeID for survey "+ str(surveyNumber)+" is "+ str(SurveyDetails["QuotaCalculationTypeID"]))
            # Check if QuotaCalculationType = Prescreens
        if SurveyDetails["QuotaCalculationTypeID"] == 1:
            TotalRemainingQuota = SurveyQuota["Quota"] - SurveyQuota["Completes"]
            # Check if QuotaCalculationType = Prescreens
        elif SurveyDetails["QuotaCalculationTypeID"] == 2:
            TotalRemainingQuota = SurveyQuota["Quota"] - SurveyQuota["Prescreens"]
            break  
        # Final data to be kept in Output file
        surveyNumberDetails = [surveyNumber, SurveyDetails["SurveyName"], SurveyDetails["SurveyStatusCode"], SurveyDetails["CountryLanguageID"], SurveyDetails["QuotaCPI"], 
                               SurveyDetails["BidLengthOfInterview"], SurveyQuota["Quota"], SurveyQuota["Prescreens"], 
                               SurveyQuota["Completes"], TotalRemainingQuota, 
                               SurveyDetails["IsVerifyCallBack"]]
        # Append final data to final list
        finalCsvData.append(surveyNumberDetails)
with open('output.csv', 'w', newline='\n') as result:
        writer = csv.writer(result)
        for row in finalCsvData:
            writer.writerow(row)

# Let the user know the script is complete
print('Done!')