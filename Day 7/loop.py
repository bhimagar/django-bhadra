# Loop: executing same block of code multiple time

#  while loop: executing same block of code multiple time until a condition is met
# while block is executed if the condition is True
# the condition in while is checked after every execution of while block
#  if line 6 is True: kine 17, 18 execute, line 16 condition check
# end program: ctrl + c
# syntax:
# while condition:
#     statement1
#     statement2
#     statement3

# a = 0
# b = 3

# while a < b:
#     print("Hello")
#     print("World")
#     a += 1 # a = 1 + 1 = 2 + 1 =3

# #  for loop

# a = 0
# b = 5

# while a < b: # parent while block
#     print("Parent Block")
#     # if a  == 2:
#     #     break
#     a += 1
#     while a < b: # child while block
#         print("Child Block")
#         # if a == 2:
#         #     break
#         a += 1
# print("Line 30")

# nested while 

a = 0
c = 0
b = 5

while a < b: # parent while block
    print("Parent Block")
    # if a  == 2:
    #     break
    a += 1
    while a < b: # child while block
        print("Child Block")
        # if a == 2:
        #     break
        a += 1
print("Line 30")