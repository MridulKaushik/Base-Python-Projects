import requests
from twilio.rest import Client
import json
from countryinfo import CountryInfo

SID = "ACf9aff465f74852970ebba12a9c4ce3c7"
AUTH_TOKEN = "99eb2f3b70045995bdb7cfeb57521d49"
TWILIO_NUM = '+19289188078'
API_KEY = "c1707b6cf3e62d466c5874cdb93fb8a7"

GEO_URL = "http://api.openweathermap.org/geo/1.0/direct"
URL = "https://api.openweathermap.org/data/2.5/onecall"

city_name = input("Enter your City : ")
state_name = input("Enter your State : ")
country_name = input("Enter Your country : ")
print(type(city_name), type(state_name), type(country_name))
# print(",".joi)
country = CountryInfo(country_name)
country_code = country.calling_codes()

geo_params = {
    "q": f"{city_name},{state_name},{country_code}",
    "appid": API_KEY
}

responses = requests.get(url=GEO_URL, params=geo_params)
responses.raise_for_status()
lat_data = responses.json()[0]["lat"]
long_data = responses.json()[0]["lon"]

params = {
    "lat": lat_data,
    "lon": long_data,
    "exclude": "alerts,minutely,daily",
    "appid": API_KEY
}

response = requests.get(url=URL, params=params)
response.raise_for_status()
data = response.json()

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)


will_rain = False

for _ in range(0, 12):
    condition_code = data["hourly"][_]["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(SID, AUTH_TOKEN)
    message = client.messages \
                    .create(
                         body="Bring your Umbrella ☂️\nToday it might rain",
                         from_=TWILIO_NUM,
                         to='+919555355039'
                     )

    print(message.sid)
    print(message.status)
