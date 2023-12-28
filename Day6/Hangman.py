import random 
import Hangman_art
import Hangman_word_list

print(Hangman_art.logo)
# List of words to choose randomly from.
#word_list = ["ardvark", "baboon", "camel"]
# Choosing a random word from word list.
rand_word = random.choice(Hangman_word_list.word_list)
print(rand_word)
# List for Hangman word
display = []
for j in rand_word:
    display.append("_")
# Variable for lives
lives = 6
i = 0
while i < len(rand_word):
    # Taking the user input.
    guess = input("Guess A letter: ").lower()

    # Looping through each letter in the random word and checking if the letter choosen by user matches.
    # And Each time it matches we print Right and if not the Wrong
    """for i in rand_word:
        if i == guess:
            print("Right")
        else:
            print("Wrong")"""

    # Make list of underscore 

    # Substiutes the user's right guess in display list
    num = 0
    for k in rand_word:
        num += 1
        #Reducing lives on wrong guess
        if k == guess:
            display[num-1] = guess
    if guess not in rand_word:
        lives -= 1
        print("You guessed the wrong letter")
        print(Hangman_art.stages[lives])
        # Reduce live if guess is not right
    string_disp = ""
    for letter in display:
        string_disp += letter
    print(string_disp)
    if lives == 0:
         i = len(rand_word)
         print("You Lose")
    elif "_" not in display:
        i = len(rand_word)
        print("You Win")




    