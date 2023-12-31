import art
# Functions for Add Subtract ,Devide and Multiply  .
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def devide(a, b):
    return (a / b)
def multi(a , b):
    return a * b
# Calc Input

#Calc Dictionary
def calculator():
    # Calc Input
    print(art.logo)
    a = float(input("Enter first number: "))
    dict_calc = {
                "+": add,
                "-": sub,
                "/": devide,
                "*": multi
                }

    for operator in dict_calc:
        print(operator)

    more = False
    while more == False:
        operation = input("Choose an operation symbol: ")
        b = float(input("Enter second number : "))
        result = dict_calc[operation](a,b)

        print(f"{a} {operation} {b} = {result}")
        more_calc = input(f"Press Enter if want to continue calculating with the result {result} or y to start new calculation or n to exit: ")
        if more_calc == "":
            a = result
        elif more_calc == "y":
            calculator()
        elif more_calc == "n":
            more = True

calculator()