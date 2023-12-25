import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = int(input(("What do you choose ? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")))
Comp_choice = random.randint(0, 2)

print("Your Choice")
if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
elif choice == 2:
    print(scissors)

print("Computer Choice")
if Comp_choice == 0:
    print(rock)
elif Comp_choice == 1:
    print(paper)
elif Comp_choice == 2:
    print(scissors)

if choice == Comp_choice :
    print("Draw")
elif choice == 0 and Comp_choice == 1:
    print("You lose")
elif choice == 0 and Comp_choice == 2:
    print("You win")
elif choice == 1 and Comp_choice == 0:
    print("You win")
elif choice == 1 and Comp_choice == 2:
    print("You lose")
elif choice == 2 and Comp_choice == 0:
    print("You lose")
elif choice == 2 and Comp_choice == 1:
    print("You win")

