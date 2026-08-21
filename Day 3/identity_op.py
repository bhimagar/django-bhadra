# Identity operator: check if two variables refers to same address
a = 10
b = 10
c = 15
d = 15

print(id(a))
print(id(b))
print(id(c))

# is: if two varibales erfers to same address -> Output: True else False
print(a is b)
print(a is c)
print(c is d)

# is not: if two varibales erfers to same address -> Output: False else True
print(a is not b)
print(a is not c)
print(c is not d)
