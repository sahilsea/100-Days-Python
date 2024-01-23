# Unlimited Positional Arguments 
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum 

print(add(1,3,5,1,2,1))

# Unlimited Keyword Arguments
def multi(**kwargs):
    print((kwargs))

multi(summ = 1, multii = 5)