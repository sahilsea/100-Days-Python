"""n = number of operations"""
"""BigO is a measure of the worst case or the highest number of operations."""


# BigO(n) linear.
# How It works : The num of operations is same as the number of data passed.
# Efficiency: linear
def print_items(n):
    for i in range(n):
        print(i)

# BigO(n) DropConstant. Here we drop constant for 2n to n.
# How It works : The num of operations is same as the number of data passed.
# Efficiency: linear
def DCprint_items(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)

# BigO(n^2). here we get squared num of items print out then we pass.
# How it Works: Like we passed 10 and got hundred items.
# Efficiency: Much less efficient in Time complexity compared to linear BigO(n).
def n2print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

# BigO Drop Non- Dominants.Here we drop the values that are non-dominants.
# How it Works: O(n^2 + n) as the value of n increases the vastness of n becomes insignificient as compared to n^2 so we drop n.
# Efficiency : Same as BigO(n^2).
def DnDprint_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
    
    for k in range(n):
        print(k)


# Big0(1) - Best case for BigO
# How it works: The number of operations is always constant.
# Efficiency : Most Efficient for BigO
def add_items(n):
    return n + n + n

# BigO(log n) - Next Best case for BigO
# Num of Operations : log n for ex - we need to search for an item in a list of 64 item then the number of operations will be log 2 64 = 6.
# Efficiency : Next Best Efficient then BigO(1)
