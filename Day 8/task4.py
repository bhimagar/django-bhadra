# 1. Review system, the stars typically represent the different levels of satisfaction.
# Start by creating a rating variable and set it equal to a decimal number.
# Make a rating system using an if/elif/else statement:
# rating greater than 4.5, print 'Extraordinary'
# rating greater than 4, print 'Excellent'
# rating greater than 3, print 'Good'
# rating greater than 2, print 'Fair'
# Everything else, print 'Poor'

# rating = float(input("Give rating (1 to 5):"))

# if  rating > 4.5:
#     print("Extraordinary")
# elif rating > 4:
#     print("Excillent")
# elif rating > 3:
#     print("Good")
# elif rating > 2:
#     print("Fair")
# else:
#     print("Poor")



# 2. Use the random module to create a number from 0 to 5.
# Then use an if/elif/else statement to print out one of these six random facts:
# 0 - 'Flamingos turn pink from eating shrimp.'
# 1 - 'The only food that doesn\'t spoil is honey.'
# 2 - 'Shrimp can only swim backwards.'
# 3 - 'A taste bud\'s life span is about 10 days.'
# 4 - 'It is impossible to sneeze while sleeping.'
# 5 - 'It is illegal to sing off-key in North Carolina.'

# import random

# number = random.randint(0, 5)

# if number == 0:
#     print("Flamingos turn pink from eating shrimp.")
# elif number == 1:
#     print("The only food that doesn\'t spoil is honey.")
# elif number == 2:
#     print("Shrimp can only swim backwards.")
# elif number == 3:
#     print("A taste bud\'s life span is about 10 days.")
# elif number == 4:
#     print("It is impossible to sneeze while sleeping.")
# elif number == 5:
#     print("It is illegal to sing off-key in North Carolina.")



# 3. Instructions
# four seasons in the year — winter, spring, summer, or fall
# Ask the user the month number using the input() function.
# Check for the four seasons using an if/elif/else statement and logical operators:
# month is 1, 2, 3, print 'Winter'
# month is 4, 5, 6, print 'Spring'
# month is 7, 8, 9, print 'Summer'
# month is 10, 11, 12, print 'Autumn'
# Everything else is 'Invalid'

# month = int(input("Month:"))

# if month == 1 or month == 2 or month == 3:
#     print("Winter")
# elif month == 4 or month == 5 or month == 6:
#     print("Spring")
# elif month == 7 or month == 8 or month == 9:
#     print("Summer")
# elif month == 10 or month == 11 or month == 12:
#     print("Autumn")
# else:
#     print("Invalid")



# 4. Create a weight conversion program that:
# Asks the user what their Earth weight is (as a float).
# Asks the user for a planet number (as an int).
# Then, use an if/elif/else statement to calculate the user's weight on the destination planet.
# To calculate the user's weight:
# destination weight=Earth weight × relative gravity
# Number	Planet	Relative Gravity
# 1	Mercury	0.38
# 2	Venus	0.91
# 3	Mars	0.38
# 4	Jupiter	2.53
# 5	Saturn	1.07
# 6	Uranus	0.89
# 7	Neptune	1.14
# If the user enters a planet number outside of 1 - 7, print a message that says 'Invalid planet number'.

# weight = float(input("Earth weight:"))
# number = int(input("Planet number:"))

# if number == 1:
#     print(weight * 0.38)
# elif number == 2:
#     print(weight * 0.91)
# elif number == 3:
#     print(weight * 0.38)
# elif number == 4:
#     print(weight * 2.53)
# elif number == 5:
#     print(weight * 1.07)
# elif number == 6:
#     print(weight * 0.98)
# elif number == 7:
#     print(weight * 1.14)
# else:
#     print("Invalid planet number")
    
    

# 6. a countdown from 10 to 1.
# Use a for loop that counts down by using the "step" value in range().
# Inside the loop, print the numbers from 10 to 1, each on its own line.
# When the loop finishes the countdown, print this exact string.

# for number in range(10, 0, -1):
#     print(number)

# print("Hello")



# 7. Suppose we have a pair of dice.
# First, use the random module to “roll” the two dice.
# Each die (named die1 and die2) should have an integer value from 1 to 6.
# Store the sum of the two random values in variable named total.
# Using a while loop, check if total is 2. If it isn't, print the string 'Nope' and keep "rerolling" the dice.
# Let the loop run until the total is 2, then print 'Snake eyes!

# import random

# die1 = random.randint(1, 6)
# die2 = random.randint(1, 6)

# total = die1 + die2

# while total == 2:
#     print("Nope")
    
#     die1 = random.randint(1, 6)
#     die2 = random.randint(1, 6)
#     total = die1 + die2
    
# print("Snake eyes")    

# For loop
# 8. Find the sum of numbers from 1 to 100
# total = 0

# for i in range(1, 101):
#     total = total + i

# print(total)

# 9. Find the sum of even numbers from 1 to 50
# total = 0

# for i in range(2, 51, 2):
#     total = total + i
    
# print(total)

# 10. Find the sum of odd numbers from 1 to 50
# total = 0

# for i in range(1, 51, 2):
#     total = total + i
    
# print(total)

# 11.  create a list of numbers. Find sum of all numbers in the list
# numbers = [1, 2, 3, 4, 5, 6, 7]
# total = 0

# for number in numbers:
#     total = total + number
    
# print(total)

# 12. define a word and print out each character
# word = "mindriser"

# for character in word:
#     print(character)

# 13.  create a list of numbers. find the largest number
# num = [1, 20, 22, 333, 44, 555]

# largest = num[0]

# for number in num:
#     if number > largest:
#         largest = number

# print(largest)

# 14. create a list of numbers and count how many even numbers exist
num = [1, 2, 3, 4, 5]

count = 0

for number in num:
    if number % 2 == 0:
        count = count + 1
        
print(count)