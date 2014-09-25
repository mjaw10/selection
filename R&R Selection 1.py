#matthew wadkin
#24/09/17
#this program will tell the user if they are old enough to vote
#and how long it is until they can retire

age = int(input("How old are you: "))
if age >= 18:
    print("You are old enough to vote")
else:
    print("You are not old enough to vote")

retire = 65 - age
print("You can retire in {0} years".format(retire))
