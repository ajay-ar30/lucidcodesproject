import json

with open('survey.json') as infile:
    data = json.load(infile)
    #print the value of SurveyName key from Survey object
    print(data['Survey']['SurveyName'])
    #updating key values
    data['Survey']['SurveyName'] = "Ajay's Survey" 
    data['Survey']['CountryLanguageID'] = '9'
    data['Survey']['SurveyStatusCode'] = '03'
    #printing all the contents stored in data variable
    print(data) 
    #opening a new file in write mode with outfile as it's name
    with open('week3_hw_survey.json', 'w') as outfile: 
        #storing updated values of data variable in outfile variable
        json.dump(data, outfile) 
