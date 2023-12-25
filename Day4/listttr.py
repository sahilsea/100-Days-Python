# List is a data structure used to store multiple datas in one seqence of memory in an order.


rl_fruits = ["Apple", "Oranges", "Mangos", 123]
print(rl_fruits[3])
#Negative indexing
print(rl_fruits[-1])
print(rl_fruits[-2])
print(rl_fruits)


# Changing elements
rl_fruits[1] = 453
print(rl_fruits[1])
print(rl_fruits)

# Appending elements
rl_fruits.append(233)
print(rl_fruits)

# There are many other functions
rl_fruits.extend([233, 189, 23, 98])
print(rl_fruits)

rl_fruits.pop()
print(rl_fruits)

print(len(rl_fruits))