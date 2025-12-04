import requests

def quest():
    try:
        Complete_link = "https://bored-api.appbrewery.com/random"
        response = requests.get(Complete_link)
        return response.json()['activity']
    except:
        return "Please try again!"

print(quest())