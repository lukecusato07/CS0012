# Project 1 Part 1
from random import randint

print("You have the following two choices:")
print("Option 1: Cooperate with the authorities")
print("Option 2: Stay silent")

partnerAChoice = int(input("Enter 1 or 2: "))
partnerBChoice = randint(1,2)

print("You chose: ", partnerAChoice)
print("The computer chose: ", partnerBChoice)
print("\n")


# 5 runs: DONE!
# partnerAChoice needs to be randint(): DONE!
# We need a loop for the amount of runs --> number = count controlled --> for loop: DONE!
# Need variables to get the count:
# partnerACount and partnerBCount
# Need to print out:
# total amount of years for partnerA and for partnerB
# average amount of years for partnerA and partnerB

# for part 2: runs = what the user wants --> input
runs = 5

# Make sure runs is between 10 and 500
# Condition:
# Can't be less than 10
# Can't be more than 500
# while condition (is true --> true is the default):
    # Do this
while runs < 10 or runs > 500:
    # Do this
    # Tell the user they need to try again
    # Let them give their input again for the amount of runs they want

partnerAChoice = randint(1,2)
partnerACount = 0
partnerBCount = 0

# Runs --> the amount that we do it
for count in range(runs):
    # What we do goes here
    # Put partnerAChoice inside the loop --> can't just do partnerAChoice
    # You've done the work to put it in the loop and you need randint somewehre in here
    # Same for partner B

    # Increase the count in terms of the choice made --> for both partners
    x = 10
    x += 5

# Now I should have both partners counts
# Tell me how many years each partner is doing in prison
# We need to print out the averages of their count
# Average total / times we ran the trial
# --> average prison time for partner a and partner b


