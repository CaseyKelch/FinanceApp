import requests
import json
import keyring

ticker = input("What is the ticker?")
yahoo_url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/qu/quote/{0}/financial-data".format(ticker)
yahoo_key = keyring.get_password("yahoo", "api_key")
headers = {
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com",
    'x-rapidapi-key': yahoo_key
    }

r = requests.request("GET", yahoo_url, headers=headers)

json_data = r.text
financial_data = json.loads(json_data)
json_formatted_str = json.dumps(financial_data, indent=2)

# with open("financials.json", "w") as f:
#     f.write(str(json_formatted_str))
print(financial_data["financialData"]["targetHighPrice"]["fmt"])
