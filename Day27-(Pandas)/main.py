with open("weather_data.csv",mode= 'r') as weather_data:
    data = weather_data.readlines()
    print(data)
import csv 

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != 'temp':
            temperatures.append(int(row[1]))
    print(temperatures)

import pandas

# Reading the Weather data and creating a list of all the temp.
data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])
temp_list = data['temp'].to_list()
# print(temp_list)

#Challange = Average Temperature
total_temp = 0
for temperature in temp_list:
    total_temp += temperature
avg_temp = total_temp/len(temp_list)
print(avg_temp)

# Average Temp in Pandas
print(data['temp'].mean())

# Challange - Others methods in Pandas
print(data['temp'].max())
print(data['temp'].mode())

# Get Data in columns
print(data['condition'])
print(data.condition)

# Get Data in row
data_in_row = data[data.day == 'Monday']
print(data_in_row)

# Challange - Pull out max day temp of the week in row
data_in_row = data[data.temp == data['temp'].max()]
print(data_in_row)

# Challange - Convert the temp of Monday to Faranheit
monday = data[data.day == 'Monday']
mon_temp = monday.temp[0]
mon_temp_in_Farh = mon_temp * 9/5 +32
print(mon_temp_in_Farh)

# Creating DataFrame 
data = {
    "Students": ["Amy", "James", "Srinity"],
    "Score": [55, 32, 90]
}
students_data = pandas.DataFrame(data)
print(students_data)
students_data.to_csv("student_data.csv")

import pandas

# Challange - Create a csv file containing num of colors of squarrel types.
# Reading the squl file and storing it in data variable
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240120.csv")

# Getting the num of sqrl of particular color.
num_of_gray_sqrl = len(data[data['Primary Fur Color'] == 'Gray'])
num_of_black_sqrl = len(data[data['Primary Fur Color'] == 'Black'])
num_of_sqrl = len(data['Primary Fur Color'])
num_of_red_sqrl = num_of_sqrl - (num_of_black_sqrl + num_of_gray_sqrl)

# Storing all color of squrl data in dict.
sqrl_data = {
    "Fur Color": ['Gray','Black','Red'],
    "Count": [num_of_gray_sqrl, num_of_black_sqrl, num_of_red_sqrl]
}
sqrl_count_data = pandas.DataFrame(sqrl_data)
sqrl_count_data.to_csv('Squirrel_color_count.csv')



