# Welcome 
print("Welcome to the tip calculator.")
# Total Bill
bill = int(input("What is your total bill? " + "$"))
# Number of people to Split the Bill 
numOfPpl = int(input("How many people to Split the bill? "))
# Percentage to Tip
tip = int(input("What percentage would you like to tip? "))
# Each Person should pay
pay = (((bill+((tip)/100))/numOfPpl))
print (f"Each person should pay: ${pay}")