#TODO: Create a letter using starting_letter.txt 
letter_all_name = []
letter_name = ''
with open("../Mail Merge Project Start/Input/Names/invited_names.txt") as all_names:
    for namm in all_names.readlines():
        letter_all_name.append(namm)

raw_letter_content = "Dear [name], \nYou are invited to my birthday this Saturday.\nHope you can make it!\nAngel"

#for each name in invited_names.txt
for name in letter_all_name:
    with open(f"../Mail Merge Project Start/Output/ReadyToSend/{name}letter.txt", mode= "w") as letter:
        letter_content_added_name = raw_letter_content.replace("[name]", name)
        letter_content_removed_nline = letter_content_added_name.strip()
        letter.write(letter_content_removed_nline)
#Replace the [name] placeholder with the actual name.
    # for name in all_names:
    #     letter_name = name
#Save the letters in the folder "ReadyToSend".

