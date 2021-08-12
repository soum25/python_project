from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import os
import requests

#twilio

TWILIO_ACCOUNT_SID = os.environ.get("MY_TWILIO_ACCOUNT_SID")


account_sid = TWILIO_ACCOUNT_SID
auth_token = os.environ.get("AUTH_TOKEN")


MY_LAT = 48.801780
MY_LNG = 2.370600

api_key = os.environ.get("API_KEY")

parameters = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "exclude": "current,minutely,daily",
    "appid": api_key
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
print(response.status_code)
weather_data = response.json()["hourly"]

will_rain = False
for data in weather_data:
    filter_id_data = data["weather"]
    for datas in filter_id_data:
        condition_code = int(datas["id"])
        if condition_code < 700:
            will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Bring your Umbrella!!!.",
        from_="your twilio_number',
        to='your_number'
    )

    print(message.status)
