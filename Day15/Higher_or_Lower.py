import random
import logo
from game_data import data

game_over = False
print(logo.logo)
score = 0


while game_over == False:
    # Random Index
    rndm_index = random.randint(0, len(data)-1)
    rndm_index_2 = random.randint(0, len(data)-1)
    # Follower Count a
    a = data[rndm_index]['follower_count']

    # Follower a Discription
    print("")
    print("")
    a_dis = f"Compare A = {data[rndm_index]['name']} a {data[rndm_index]['description']} from {data[rndm_index]['country']} "
    print(a_dis)

    # VS logo
    print(logo.vs)

    # Follower Count b
    b = data[rndm_index_2]['follower_count']

    # Follower b Description
    b_dis = f"Against B = {data[rndm_index_2]['name']} a {data[rndm_index_2]['description']} from {data[rndm_index_2]['country']} "
    print(b_dis)

    # For Checking
    print(f"a = {a} , b = {b}")

    # Player's answer
    answer = input("Who has more followers, a or b ? ")

    # Testing The answer
    if answer == 'a' and a > b:
        score += 1
        print(f"You are right! Current Score: {score}.")
    elif answer == 'b' and b > a:
        score += 1
        print(f"You are right, Current Score: {score}.")
    else:
        print(f'Game Over!, your total score is {score}.')
        game_over = True

    