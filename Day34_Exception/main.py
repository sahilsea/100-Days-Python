# # FileNotFoundError
# with open("filexp.txt") as file:
#     file.read()

# # List index out of range
# listt = [1, 3, 4]
# print(listt[3])

# # Syntax Error
# print("shila"

# # Type Error
# print(5 + "str")

# # Key Error
# food = {"fruits": ["apple", "banana"],
#         "veggis": ["bringle", "onion"]}
# print(food["apple"])

try:
    file = open("filexp.txt")
    food = {"fruits": ["apple", "banana"],
        "veggis": ["bringle", "onion"]}
    print(food["fruits"])
except FileNotFoundError:
    file = open("filexp.txt", mode= "w")
except KeyError:
    print('The key does not exist')
else:
    content = file.read()
    print(content)
finally:
    file.close()