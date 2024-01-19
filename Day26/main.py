# # Open and read file normally
# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# # Open and read file temporarly
# with open("my_file.txt") as file:
#     content = file.read()
#     print(content)

# # Open and write file temporarly
# with open("my_file.txt",mode = "w" ) as file:
#     file.write("New Text")

# Open and append file temporarly
with open("my_file.txt",mode = "a" ) as file:
    file.write("\nNew Text Append")

# # Write and append mode creates new file if the file mentioned don't exist
# with open("new_file.txt", mode = "a") as newfile:
#     newfile.write("\n Creating new file ")
