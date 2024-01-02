import random

Attempts = 0
print ("Welcome to Random number Guessing Game.")
Difficulty = input("Choose a difficulty : 'easy' or 'hard' :")
print ("I am guessing a number between 1 and 100")
random_num = random.randint(1, 100)
if Difficulty == "easy":
    Attempts = 10
elif Difficulty == "hard":
    Attempts = 5
print(f"You have {Attempts} Attempts to guess the number")

Status = True
while Status == True:
    Guess = int(input("Enter your Guess: ")) 

    if Guess == random_num:
        print("You Win!")
        Status = False
    elif Guess > random_num:
        print("Your Guess is too High")
        Attempts -= 1
    elif Guess < random_num:
        print("Your guess is too low")
        Attempts -= 1

    if Attempts == 0:
        Status = False
        print("You Lose!")
        print(f"The right no is {random_num}")




