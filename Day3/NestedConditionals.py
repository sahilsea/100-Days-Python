print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    age = int(input("What is your age? "))
    if age < 12:
        print("You can ride the rollercoaster!, you need to pay 10$")
    elif age <= 18:
        print("You can ride the rollercoaster!, you need to pay 15$")
    else:
        print("You can ride the rollercoaster!, you need to pay 20$")
else:
    print("Sorry you must be taller then 120cm to ride the rollercoaster.")