from datetime import datetime
import pandas
from random import choice
import smtplib
##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
# Getting the day and the month.
current_day = datetime.now()
day = current_day.day
month = current_day.month
# print(f"month: {month}, day: {day}")

# Reads the birth data and converts it to dictionary
birth_data = pandas.read_csv("birthdays.csv")
birth_dict_data = birth_data.to_dict(orient="records")
# print(birth_dict_data[0]['name'])
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

for i in range(0 ,len(birth_dict_data)):
    if month == birth_dict_data[i]['month'] and day == birth_dict_data[i]['day']:
        # Birthday Boy info
        name_bdy_boy = birth_dict_data[i]['name']
        email_bdy_boy = birth_dict_data[i]['email']
        # Choosing a random letter
        random_txt_letter = choice(["./letter_templates/letter_1.txt", "./letter_templates/letter_2.txt", "./letter_templates/letter_3.txt"])
        # Opens the random letter and reads and then replaces the name and writes from the updated file.
        with open(random_txt_letter, mode= 'r') as random_letter:
            filedata = random_letter.read()
            filedata = filedata.replace('[NAME]',name_bdy_boy )
        # print(email_bdy_boy)

# 4. Sends the letter generated in step 3 to that Birthday boy email address.
        my_email = "bewmow@gmail.com"
        my_password = "abde9dals322#2"
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user= my_email, password= my_password)
        connection.sendmail(from_addr= my_email, to_addrs= email_bdy_boy, msg= f"Subject: Happy Birthday \n\n {filedata}")
        connection.close()






