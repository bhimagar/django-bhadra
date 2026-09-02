# function: like variable but instead of storing value, it stores block of code
# every function has specific task
# reuseable, remove duplication

# syntax:
# def function_name(): # function define
#     block of code

# function_name() # function call

# requirement: print out the introduction of the user
# def intro(): # function define
#     print("I am Bhim.") # static data
    
# intro() # function call

# intro() # function call

# parameter: variables defines in the parathesis during function defination
# arguments: variable/data defined inside the parathesis during function call
# arguments are accepted by parameter

# types of arguments
# positional argument: arguments accepts sequencial according to their position by thr parameter

# def intro(name, age, address): # name is a parameter
#     print(name)
#     print(f"I am {name}. I am {age} years old. I am from {address}")

# a = "Bhim Magar"
# b = 22
# intro(b, a, "ktm") # a is a argument

# keyword argument: parameter are called and data are assigned to the parameter directly during function call

# def intro(name, age, address):
#     print(name)
#     print(f"I am {name}. I am {age} years old. I am from {address}")

# a = "Bhim Magar"
# b = 22
# intro(address="ktm", name=a, age=b)

# defualt argument: a defualt data is assigned to the parameter
# defualt data are used incase the arguments are not provided

def intro(name = "Defualt_name", age = "Defualt_name", address = "Defualt_address"):
    print(name)
    print(f"I am {name}. I am {age} years old. I am from {address}")

a = "Bhim Magar"
b = 22
intro(b, a, "ktm")

# print("I am name")
# print("I am", a, "hello", b)
# print("I am" + a + "hello" + b) # concatination
# print(f"I am" + a + "hello" + b) # f
# print(f"I am" + {a} + "hello" + {b}) # { }

# todo
# create a function add 2 parameter
# the function should add 2 parameter and provide the result
# get 2 numbers from user and use it as arguments during function call

# create a function add 2 parameter
# the function should subtract 2 parameter and provide the result
# get 2 numbers from user and use it as arguments during function call

# create a function add 2 parameter
# the function should multiply 2 parameter and provide the result
# get 2 numbers from user and use it as arguments during function call

# create a function add 2 parameter
# the function should divide 2 parameter and provide the result
# get 2 numbers from user and use it as arguments during function call