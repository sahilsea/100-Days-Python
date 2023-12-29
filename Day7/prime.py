number = int(input("Enter a number to check if it is prime or not: "))
is_prime = True
for i in range(2, number):
    if number % i == 0:
        is_prime = False

if is_prime:
    print("Number is Prime")
else:
    print("Not Prime")
    