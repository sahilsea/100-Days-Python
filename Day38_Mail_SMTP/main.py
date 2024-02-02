import smtplib

my_email = "sa@gmail.com"
my_password = "chfsjmhdgjhv"

with (smtplib.SMTP("smtp.gmail.com")) as connection:
    connection.starttls()
    connection.login(user= my_email, password= my_password)
    connection.sendmail(from_addr= my_email, to_addrs= "skumarbca2022@ismpatna.ac.in", msg= "Subject:Hello\n\n Hii there, it me from sending mail from python")


# # Datetime module
# import datetime as dt 

# current_date = dt.datetime.now()
# year = current_date.year
# month = current_date.month
# day = current_date.day
# weekdayy = current_date.weekday
# print(weekdayy)
