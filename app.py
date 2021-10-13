import requests

term = str(input("Please enter the term: "))

url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define" #URL of API

#Makeing query that we want to search
querystring = {"term":str(term)}

headers = {
    'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
    'x-rapidapi-key': "5c42c03828mshc340236c62604fep162f35jsnafb5fcd1ae4a" #You can use your own API key
    }

response = requests.request("GET", url, headers=headers, params=querystring)

#Save data to file part
saveIntoFile = str(input("Do you want to save response into text file(y/n): "))

if saveIntoFile == "y":
    textFile =  open(term + ".txt", "w")
    textFile.write(response.text)
    textFile.close()
elif saveIntoFile == "n":
    print(response.text)
elif saveIntoFile != "y" or "n":
    print("You haven't enter y or n, please try again!")
