import requests
import json
import keyring

# Should convert functions into Class
api_key = keyring.get_password("yahoo", "api_key")


def key_stats(ticker):
    url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/qu/quote/{0}/default-key-statistics".format(ticker)
    headers = {
        'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
        'x-rapidapi-key': api_key
    }
    r = requests.request("GET", url, headers=headers)
    json_data = r.text
    data = json.loads(json_data)

    return data


def stock_profile(ticker):
    url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/qu/quote/{0}/asset-profile".format(ticker)
    headers = {
        'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
        'x-rapidapi-key': api_key
    }
    r = requests.request("GET", url, headers=headers)
    json_data = r.text
    data = json.loads(json_data)

    return data


def financial_data(ticker):
    url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/qu/quote/{0}/financial-data".format(ticker)
    headers = {
        'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
        'x-rapidapi-key': api_key
    }
    r = requests.request("GET", url, headers=headers)
    json_data = r.text
    data = json.loads(json_data)

    return data
