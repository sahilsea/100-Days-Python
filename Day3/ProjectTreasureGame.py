print("Welcome to Treasure Island Your Mission is to find the treasure")


lr = input("Which direction you wanna go type L for left or R for right: ")
if lr == "R" or lr == "r":
    print("You Died")
elif lr == "L" or lr == "l":
    sw = input("You are near a river , Do you wanna Swim or Wait type S for Swim and W for Wait: ")
    if sw == "S" or  sw == "s":
        print("You Died Swimming")
    elif sw == "W" or sw == "w":
        door = input("There are Three doors here , Red , Blue and Yellow , Which one do you want to open , Type R for Red , B for Blue and Y for Yellow door: ")
        if door == "R" or door == "r" or door == "B" or door == "b":
            print("Game over.")
        else:
            print("You Win!")
            print('''          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK] ''')
