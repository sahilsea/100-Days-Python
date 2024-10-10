# def add (n1, n2):
#     return n1 + n2

# def subtract(n1, n2):
#     return n1 - n2

# def multiply(n1, n2):
#     return n1 * n2

# def devide(n1, n2):
#     return n1/n2

# def calculate(calc_function, n1, n2):
#     return calc_function(n1, n2)

# result = calculate(multiply, 3 , 2)
# print(result) 

# def outer_function():
#     print("I am outer")
    
#     def nested_function():
#         print("I am inner")

#     return nested_function  
    
# inner_function = outer_function()
# inner_function()

## Python decorator function
# import time
# def delay_decorator(function):
#     def wrapper_function():
#         time.sleep(2)
#         function()
#         function()
#     return wrapper_function

# @delay_decorator
# def say_hello():
#     print("hello")


# import time 

# def delay_decorator(function):
#     def wrapper_function():
#         time.sleep(2)
#         function()
#     return wrapper_function

import time
current_time = time.time()
# print(current_time) # seconds since Jan 1st, 1970 

# Write your code below 👇

def speed_calc_decorator(function):
  def wrapper_function():
      function()
      function()
  return wrapper_function
  

@speed_calc_decorator
def fast_function():
  for i in range(1000000):
    i * i
  print(current_time)

        
@speed_calc_decorator
def slow_function():
  for i in range(10000000):
    i * i
  print(current_time)