# Logical Operator: Output: Boolean
a = 10
b = 10
c = 5

# and: if all condition are True, output: True, else False
# print(True and False and True)
print(a == b and a < c) # False

# or: if all/any one condition is True, output: True, else False
# print(True or False or True)
print(a == b or a < c or b > c) # True

# not: if condition is True output is False, and vise versa
# print(not(True))
# print(a == b a < c) # False
print(not(a == b and a < c) and b < c) # False