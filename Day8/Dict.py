prog_dict = {"loop": "Doing thing over and over again",
            "list": "Data structure",
            "function": "Stores a set of instruction" }


for i in prog_dict:
    print(prog_dict[i])

#Adding new item
prog_dict["variable"] = "An intity that holds the memory address of some data"
print(prog_dict["variable"])

#Editing an item
prog_dict["variable"] = "An entity that holds the memory address of some data stored inside the system."
print(prog_dict["variable"])

