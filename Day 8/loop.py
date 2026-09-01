# break: loop end
# despite the while condition being True, break end and the loop
# if a is 2 then end the loop

# a = 0
# b = 3

# while a < b:
#     print("Hello")
#     if a == 2:
#         break
#     a += 1 # a = 1 + 1 = 2 + 1 =3

# continue loop: execution of all statements in while block
# incomplete loop: execution of statements half way
# continue: skip current loop and start new loop

a = 0
b = 3

while a < b:
    a += 1
    print("Hello World")
    if a == 2:
        continue
    # a += 1 # a = 1 + 1 = 2 + 1 =3
print("Line 11")

