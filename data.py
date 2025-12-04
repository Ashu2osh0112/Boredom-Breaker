import requests


def quest():
    Complete_link = "https://bored-api.appbrewery.com/random"
    response = requests.get(Complete_link)
    return response.json()['activity']

print(quest())