# Function without parameter
def greet():
    name = input("Enter a name: ")
    print(f"Hello {name}")
    print("What's up!")
    print("How is your Day Going")

greet()
# Function with parameter
def greet_w_para(name):
    print(f"hello {name}")

greet_w_para("Sara")

def greet_nm_location(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_nm_location("Sara", "Britain")

# Keyword arguments , here the position of the argument doesn't matter
def greet_nm_location_key(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_nm_location_key(location= "Sara", name ="Britain")