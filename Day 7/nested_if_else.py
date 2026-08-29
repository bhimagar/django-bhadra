# nested if else statement: parent and child ko concept: child block depends on parent block => parent block must be true for chold lock to be executed

# if a > b:
#     print("A is greater than B")
#     if a > b:
#         print("A is greater than B")
#     elif a < b:
#         print("B is greater than B")
# elif a < b:
#     print("B is greater than B")
#     if a > b:
#         print("A is greater than B")
#     elif a < b:
#         print("B is greater than B")
# else:
#     print("equal")
    
    
# todo:
# Drivinf licenses eligibility
# get age of user
# if user age less than 16, show user that they are not eligible
# if user age is greater than 16, show user that they are eligible
#       ask user if they have driving license(y/n)
#           if yes: print out statement
#           if no: ask if they want to get license(y/n): if yes print our statement, if no: print out statement

age = int(input("Enter your age:"))

if age > 0 and age < 16:
    print("You are not eligible to drive")
    choice = input("Will you get license in the future?(y/n)")
    if choice == "y":
        print("Good luck")
    elif choice == "n":
        print("Good luck tracelling by bus")
    else:
        print("Invalid choice")
elif age >= 16 and age <= 60:
    print("Your are eligible")
    choice == input("Do you have driving license:(y/n)")
    if choice == "y":
        print("Very Nice")
    elif choice == "n":
        print("Get ;icense soon") # ask user if that want to get license (y/n: if yes: print statement, if no: print statement)
    else:
        print("Invalid choice")
else:
    print("Please enter valid age")