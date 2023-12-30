import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# Variables to get user input
print(art.logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
shift = shift % 25
# Function for encripting the text
def ceaser(text, shift, direction):
    # Getting the index of all the text given by the user and storing it in list.
    # Shifting the index by user request by adding the shift variable
    cypher = ""
    if direction == "decode":
        shift *= -1
    for letter in text:
        if letter in alphabet:
            text_index = alphabet.index(letter) + shift
            if text_index > 25:
                new_letter = alphabet[text_index-26]
            else:
                new_letter = alphabet[text_index]
            cypher += new_letter
        else:
            cypher += letter
    print(f"Your {direction}d text is : {cypher}")

ceaser(text, shift, direction)
