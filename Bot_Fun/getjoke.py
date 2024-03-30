import requests

def getjokes():
    url = "https://world-of-jokes1.p.rapidapi.com/v1/jokes/random-joke"

    headers = {
        "X-RapidAPI-Key": "a93645818emsh99a8ce0cf75b203p1209bejsnf318c98f1ec7",
        "X-RapidAPI-Host": "world-of-jokes1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    res = response.json()
    str = ""
    str += res['title'] + "\n"
    str += res['body'] + "\n"

    return str