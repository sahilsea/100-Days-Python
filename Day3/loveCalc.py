print("The Love Calculator is calculating your score...")
name1 = input("Enter name one: ") # What is your name?
name2 = input("Enter name two: ") # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
from collections import Counter
n1 = Counter(name1.lower())
n2 = Counter(name2.lower())

numOfTrue_n1 = n1["t"] + n1['r'] + n1['u'] + n1['e']
numOfLove_n1 = n1['l'] + n1['o'] + n1['v'] + n1['e']

numOfTrue_n2 = n2["t"] + n2['r'] + n2['u'] + n2['e']
numOfLove_n2 = n2['l'] + n2['o'] + n2['v'] + n2['e']

total = int(str(numOfTrue_n1 + numOfTrue_n2) + str(numOfLove_n1 + numOfLove_n2))

if total < 10 or total > 90:
  print(f"Your score is {total}, you go together like coke and mentos.")
elif total < 50 and total > 40:
  print(f"Your score is {total}, you are alright together.")
else:
  print(f"Your score is {total}.")
  