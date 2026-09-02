# try:
#     rating = float(input("Give rating (1 to 5):"))

#     if  rating > 4.5:
#         print("Extraordinary")
#     elif rating > 4:
#         print("Excillent")
#     elif rating > 3:
#         print("Good")
#     elif rating > 2:
#         print("Fair")
#     else:
#         print("Poor")
        
# except:
#     print("Give valid rating")



# try:
#     month = int(input("Month:"))

#     if month == 1 or month == 2 or month == 3:
#         print("Winter")
#     elif month == 4 or month == 5 or month == 6:
#         print("Spring")
#     elif month == 7 or month == 8 or month == 9:
#         print("Summer")
#     elif month == 10 or month == 11 or month == 12:
#         print("Autumn")
#     else:
#         print("Invalid")
        
# except:
#     print("Give valid month")



# try:
#     weight = float(input("Earth weight:"))
#     number = int(input("Planet number:"))

#     if number == 1:
#         print(weight * 0.38)
#     elif number == 2:
#         print(weight * 0.91)
#     elif number == 3:
#         print(weight * 0.38)
#     elif number == 4:
#         print(weight * 2.53)
#     elif number == 5:
#         print(weight * 1.07)
#     elif number == 6:
#         print(weight * 0.98)
#     elif number == 7:
#         print(weight * 1.14)
#     else:
#         print("Invalid planet number")
        
# except Exception as e:
#     print(e)
    
    

try:
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

except ValueError:
    print("Give valid number")

except Exception as e:
    print(e)