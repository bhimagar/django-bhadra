# for loop 

# iterable: sequential data (group data, string)
# a = [1, 2, 3, 4, 5]

# iteration: process of moving from 1st index to last index of iterable

# iterator: variable used to perform iteration in iterable

# loops depends on the existing data in iterable

# syntax 
# for iterator in iterable:
#   statement1
#   statement2

# a = [1, 2, 3, 4, 5, "hello", "hi"]

# for i in a:
#     print("Hello World", i)
    
# nested for loop     

a = [1, 2, 4, 5, "hello", "hi"]
b = "loop"

for i in a:
    print("Hello World", i)
    for j in b:
        print(j)
# complete loop: execute