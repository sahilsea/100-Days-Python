import smtplib
from random import choice

# Datetime module
import datetime as dt 

current_date = dt.datetime.now()
year = current_date.year
month = current_date.month
day = current_date.day
# weekdayy = current_date.weekday
print(day)

with open("quotes.txt") as data_file:
    data_list = [quote for quote in data_file.readlines()]
# for i in data_list:
#     print(i)
if day == 3:
    random_motivational_quotes = choice(data_list)
    my_email = "sdlkjflksdjienm@gmail.com"
    my_password = "dsfsdfslkjdfsdfwev"

    with (smtplib.SMTP("smtp.gmail.com")) as connection:
        connection.starttls()
        connection.login(user= my_email, password= my_password)
        connection.sendmail(from_addr= my_email, to_addrs= "friendmail@ismpatna.ac.in", msg= f"Subject:Hello\n\n {random_motivational_quotes}")


# import pandas;

# data_file = pandas.read_table("quotes.txt")
# print(choice(data_file))