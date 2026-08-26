# simple calculator
# using input get two numbers from user (num1, num2)
# using input get a operator(+, =, *, /)
# if operator is +, print the sum of two numbers
# if operator is -, print the subtract of two numbers
# if operator is *, print the multiply of two numbers
# if operator is /, print the divide of two numbers

num1 = int(input("num1:"))
num2 = int(input("num2:"))
operator = input("Operator:")

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("error")