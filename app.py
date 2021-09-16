import requests

term = str(input("Please enter the term: "))

url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define" #URL of API

#Saveing input string into querystring variable so we can pass query that we want to search
querystring = {"term":str(term)}

#Our headers for API request
headers = {
    'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
    'x-rapidapi-key': "5c42c03828mshc340236c62604fep162f35jsnafb5fcd1ae4a" #This is my API key from my account that i created on rapidapi, if you want you can create your own!
    }

#Sends API request to URL specified on top of code with headers and query string
response = requests.request("GET", url, headers=headers, params=querystring)

#This part asks person should repsponse be saved in a file or not, if not response will be printed in console
saveIntoFile = str(input("Do you want to save response into text file(y/n): "))

if saveIntoFile == "y":
    textFile =  open(term + ".txt", "w")
    textFile.write(response.text)
    textFile.close()
elif saveIntoFile == "n":
    print(response.text)
elif saveIntoFile != "y" or "n":
    print("You haven't enter y or n, please try again!")