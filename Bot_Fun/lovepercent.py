import requests

def love(sname, fname):
    url = "https://love-calculator.p.rapidapi.com/getPercentage"

    querystring = {"sname": sname, "fname": fname}

    headers = {
        "X-RapidAPI-Key": "a93645818emsh99a8ce0cf75b203p1209bejsnf318c98f1ec7",
        "X-RapidAPI-Host": "love-calculator.p.rapidapi.com"
    }

    data = requests.get(url, headers=headers, params=querystring)
    res = data.json()

    str = "The love percentage between the given two persons is " + res['percentage']

    return str