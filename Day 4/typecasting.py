# Typecassting: process converting a datatype into another

a = 50
print(type(a))
print(a + 3)

# convert into string (str())
str_a = str(a)
print(type(str_a))
print(str_a + "3")

# COnvert into interger (int())
b = "100"
print(type(b))
int_b = int(b)
print(type(int_b))

# convert into float (float())
float_b = float(b)
print(type(float_b))
print(float_b)

# convert into list (list())
a = "Mindrisers"
# list(a) or list("Mindrisers")
my_list = list(a)
print(my_list)

# convert into tuple (tuple())
my_tuple = tuple(my_list)
print(my_tuple)

# convert into set
my_set = set(my_tuple)
print(my_set)

# convert into dictionary (dict())
z = [('name', 'ram'), ('age', 35), ('contact', '12345678')]
my_dict = dict(z)
print(my_dict)