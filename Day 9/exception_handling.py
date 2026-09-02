# Exception handling: errors caused by wrong user interaction with the program are exception

# try and except block
# try: includes lines of code that raises exception
# try block is executed if no exception, but if exception raises in try block then except block is executed instead
#  a try block can have a except block but multiple erroe specific except block

try:
    a = int(input("Enter a number:")) # value error
    print(a + 5) # name error
    # print(type(a))
    # print(a + 5)
except Exception as e:
    print(e)
# except ValueError:
#     print("Enter a valid number")
# except NameError:
#     print("a not defined")
# except:
#     print("not value or name error")