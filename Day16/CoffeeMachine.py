MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
coffee = True
while coffee == True:
# Coffee Choice
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    # Cost of the Coffee
    money = int(input(f"That would be {MENU[choice]['cost']}$:  $"))

    # Account
    account = 0

    # Change

    while money < MENU[choice]['cost']:
        print(f"That is not enough money , the cost of {choice} is {MENU[choice]['cost']}$")
        money = int(input(f"That would be {MENU[choice]['cost']}$:  $"))

    if money > MENU[choice]['cost']:
        print(f"Take the change {money-MENU[choice]['cost']}$")


    # Resource uses in cappuccino
    if choice == 'cappuccino' :

        resources["water"] = resources["water"] - MENU["cappuccino"]['ingredients']['water']
        resources["milk"] = resources["milk"] - MENU["cappuccino"]['ingredients']['milk']
        resources["coffee"] = resources["coffee"] - MENU["cappuccino"]['ingredients']['coffee']
        account += 3.0
        print("Here is your cappuccino, Enjoy.")
        


    # Resource uses in latte
    if choice == 'latte' :
        resources["water"] = resources["water"] - MENU["latte"]['ingredients']['water']
        resources["milk"] = resources["milk"] - MENU["latte"]['ingredients']['milk']
        resources["coffee"] = resources["coffee"] - MENU["latte"]['ingredients']['coffee']
        account += 2.5
        print("Here is your latte, Enjoy.")

    # Resource uses in espresso
    if choice == 'espresso' :
        resources["water"] = resources["water"] - MENU["espresso"]['ingredients']['water']
        resources["milk"] = resources["milk"] - MENU["espresso"]['ingredients']['milk']
        resources["coffee"] = resources["coffee"] - MENU["espresso"]['ingredients']['coffee']
        account += 1.5
        print("Here is your espresso, Enjoy.")
    eORn = input("Do you want more , type y for yes and n for no.: ")

    if eORn == 'n':
        coffee = False
    elif eORn == 'y':
        coffee = True 