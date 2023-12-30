import art8
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
auction_data = {}
print(art8.logo)

def highest_bidder():
    highest_bidder = 0
    highest_bidder_p = ""
    for people in auction_data:
        if highest_bidder < auction_data[people]:
            highest_bidder = auction_data[people]  
            highest_bidder_p = people
    print(f"{highest_bidder_p} has won the Auction with a bid of {highest_bidder}")

more = True
while more == True:
    name = input("Enter your Name: ")
    bid = int(input("Enter your Bid: "))
    auction_data[name] = bid
    people = input("Is there More Bidder, type Enter if yes and n for no: ")
    if people == "n":
        more = False
        
        highest_bidder()
    else:
        clear_screen()
        print(art8.logo)

