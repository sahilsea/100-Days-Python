alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
# Converting text to list.
text_list = list(text)
# Getting the index of all the text given by the user and storing it in list.
# Shifting the index by user request by adding the shift variable
text_index_list = []
for i in range(0, len(text)):
    text_index = [alphabet.index(text_list[i]) + shift]
    text_index_list += text_index
# Accessing the letters from alphabet based on the Shifted index by putting the shifted index to the alphabet as a parameter.
shift_text = ""
for i in text_index_list:
    shift_text += alphabet[i]
print(shift_text)



