import requests
from datetime import datetime
import smtplib
import time



MY_LAT = 24.792480
MY_LONG = 85.007713

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

def iss_overhead():
    if iss_latitude < 29 and iss_latitude > 20 and iss_longitude < 90 and iss_longitude > 80:
        return True
    else:
        return False
    
# def darkORnot():
    # if 

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = (data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = (data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour
print(f'Sunrise: {sunrise}\nSunset: {sunset}\nCurrent_Time: {time_now}')

def isdark():
    if time_now >= sunset or time_now <= sunrise:
        return True
    else:
        return False

while True:
    time.sleep(60)
    if iss_overhead() and isdark():
        my_email = "bewmow@gmail.com"
        my_password = "abde9dals322#2"
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user= my_email, password= my_password)
        connection.sendmail(from_addr= my_email, to_addrs= "email_bdy_boy", msg= f"Look Up 👆🏻")
        connection.close()




#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



