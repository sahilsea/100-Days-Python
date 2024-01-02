import random
# List of Cards
Cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# Random Card
Rand_card = 0
# Random Choosen Card list
Rand_card_Choosen = []
Comp_Rand_card_Choosen = []

def rand_user_deck():
    for i in range(0, 2):
        Rand_card = random.choice(Cards)
        Rand_card_Choosen.append(Rand_card)
    return Rand_card_Choosen

def rand_comp_deck():
    for i in range(0, 2):
        Rand_card = random.choice(Cards)
        Comp_Rand_card_Choosen.append(Rand_card)
    return Comp_Rand_card_Choosen












print(f"User Deck: {rand_user_deck()}, Comp Deck: {rand_comp_deck()}")