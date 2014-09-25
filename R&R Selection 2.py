#Matthew Wadkin
#34/09/14
#This program will tell the user if their number is between 1 and 20

number = int(input("Please enter a number between 1 and 20: "))

if number < 1:
    print("That number is too small")
elif number > 20:
    print("That number is too big")
else:
    print("That number is within the range")
