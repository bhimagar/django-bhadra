# break: loop end
# despite the while condition being True, break end the loop
# if a is 2 then end the loop

# a = 0
# b = 5

# while a < b:
#     print("Hello World")
#     if a == 2:
#       break
#     a += 1
# print("Line 30")

# continue loop: execution of all statements in while block
# incomplete loop: execution of statements half way
# continue: skip current loop and start new loop

# a = 0
# b = 5

# while a < b:
#     a += 1
#     # print("Hello World")
#     if a == 2:
#         continue
#     print("Hello World", a)
#     # a += 1
# print("Line 30")

# nested while loop

a = 0
c = 0
b = 5

while a < b: # parent while block
    print("Parent Block")
    # if a == 2:
    #   break
    a += 1
    while c < b: # child while block
        print("Child Block")
        # if a == 2:
        #     break
        c += 1
    # print("out of child block")
print("Line 30")

# output
# Parent Block [print]
# Child Block [print1]
# Child Block [print2]
# Parent Block [print]
# Line 30