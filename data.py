import requests

def quest():
    try:
        url = "https://www.boredapi.com/api/activity/"
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            data = response.json()
            return data.get("activity", "Couldn't find an activity")

        else:
            return "API error. Try again!"

    except:
        return "Connection error. Please try again!"