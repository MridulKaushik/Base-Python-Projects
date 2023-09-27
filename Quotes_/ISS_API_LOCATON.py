import requests
import datetime as dt
import smtplib 
import time

my_gmail = "madhurhaldi@gmail.com"
g_password = "3Gul$han@123"
my_lat = 26.837385
my_long = 80.847586

def iss_locatin():

    response = requests.get(url='http://api.open-notify.org/iss-now.json')

    response.raise_for_status()

    # Getting the json data from the api
    data  = response.json()
    iss_pos = data["iss_position"]
    longitude = data["iss_position"]["longitude"]
    latitude = data["iss_position"]["latitude"]

    if my_lat+5 >= latitude and my_lat-5 <= latitude and my_long-5 <= longitude and my_long+5 >= longitude :
        return True
    
  
def is_night():
    now = dt.datetime.now()
    time = now.time().hour

    parameter = {
        "lat":my_lat,
        "lng":my_long,
        "formatted":0
    }


    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameter)
    response.raise_for_status()
    data = response.json()

    sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
    sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

    if time <= sunrise and time >= sunset:
        return True


run_machine = True

while run_machine:
    time.sleep(60)
    if iss_locatin() and is_night() :
            with smtplib.SMTP("smtp.google.com") as connection:
                connection.starttls()
                connection.login(my_gmail, g_password)
            connection.sendmail(
                from_addr=my_gmail,
                to_addrs=my_gmail,
                msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
            )


