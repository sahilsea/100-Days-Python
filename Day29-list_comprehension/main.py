# # Creating a new list from an existing list.
# numbers = [1,2,3,4,5]
# new_list = []
# for num in numbers:
#     num += 1
#     new_list.append(num)

# print(new_list)

# # Doing it through list comprehension
# nums = [1,2,3]
# new_list = [ n+1 for n in nums ]
# print(new_list)


# # List Comprehension can also be applied to String
# name = "Sahil"
# new_list2 = [n for n in name]
# print(new_list2)

# # And to Range
# new_list = [ n+1 for n in range(1, 5) ]
# print(new_list)

# # Conditional list Comprehension (A condition or boolean is added to the end)
# names2 = ["Alex", "Freddy", "Calenor", "Sahil", "Angela", "Elenor"]
# short_names = [name for name in names2 if len(name) < 6]
# print(short_names)

# long_cap_names = [n.upper() for n in names2 if len(n) > 5]
# print(long_cap_names)

# # Challange - Square all the numbers in a given list of numbers.
# numbers = [1 , 1, 2, 3, 5, 8, 13, 21, 34, 55]
# sqrd_numbers = [n*n for n in numbers]
# print(sqrd_numbers)

# # Challange - Take user input Convert it to intigers and then append the even numbers to a new list and print.
# list_of_strings = input().split(',')
# str_to_int = [int(n) for n in list_of_strings]
# result = [n2 for n2 in str_to_int if n2 % 2 == 0]
# print(result)


# Challange
# import pandas

# # data1 = pandas.read_table('file1.txt')
# # print(data1)

# with open ("file1.txt") as data:
#     data1 = [int(d) for d in data.readlines()]


# with open ("file2.txt") as dataa:
#     data2 = [int(d2) for d2 in dataa.readlines()]

# # print(data1)
# # print(data2)
# result = [num for num in data1 if num in data2]

# # for i in data1:
# #     if i in data2:
# #         result.append(i)


# # result = [num for num in data1 and data2 if data1 == data2]
# print(result)


# # Challange
# sentence = input()
# letters = sentence.split()
# result = {letter:len(letter) for letter in letters}
# # print(result)


# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = car.items()
# print(x)


# Looping through Pandas Data Frame
import pandas
data = {
    "Student": ["Amy", "Shefar", "lily"],
    "Score": [200, 320, 120]
}
students_DF = pandas.DataFrame(data)
for (indes, row) in students_DF.iterrows():
    print(row.Student)