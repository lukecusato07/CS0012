# Write your code here :-)
from random import randint
# ALLLLL of part 2 here (don't forget the import statement)

partnerACount = 0
partnerBCount = 0

# lab 3 Part 1
for count in range(runs):
    parternAChoice = randint(1,2)
    parternAChoice = randint(1,2)

    partnerACount += parternerAChoice
    partnerBCount += parternerBChoice


print("A spent", years, "in prison")
print("B spent", years, "in prison")

# Lab 3 Part 3
print('3 strategies available:')
print('1: Random')
print('2: Only-Silent')
print('3: Only-Cooperate')


partnerACount = 0
partnerBCount = 0
strategyA = (int)(input('Select a strategy for partner A: '))
while strategyA > 3 or strategyA < 1:
    print('Must enter a number between 1 and 3')
    print('Please try again')
    strategyA = int(input('Please enter a number between 1 and 3: '))
    #for x in range(num): # dont need this for loop just need to put strategies

strategyB = (int)(input('Select a strategy for partner B: '))
while strategyB > 3 or strategyB < 1:
    print('Must enter a number between 1 and 3')
    print('Please try again')
    strategyB = int(input('Please enter a number between 1 and 3: '))
#if strategyB >= 1 or strategyB <= 3:

trials = int(input('How many trials should be simulated? '))
while trials < 10 or trials > 500:
    print('No')
    trials = int(input('Please enter a number between 10 and 500 '))


#if trials >= 10 or trials <= 500:


for x in range(trials):
    if strategyA == 1:
        partnerAChoice = randint(1,2)
    elif strategyA == 2:
        partnerAChoice = 2
    else:
            #strategyA == 3
        partnerAChoice = 1

    if strategyB == 1:
        partnerBChoice = randint(1,2)
    elif strategyB == 2:
        partnerBChoice = 2
    else:
            #strategyB == 3
        partnerBChoice = 1

    if partnerAChoice == 1 and partnerBChoice == 1:
        partnerACount += 4
        partnerBCount += 4
    elif partnerAChoice == 2 and partnerBChoice == 2:
        partnerACount += 2
        partnerBCount += 2
    elif partnerAChoice == 1 and partnerBChoice == 2:
        partnerACount += 0
        partnerBCount += 6
    elif partnerAChoice == 2 and partnerBChoice == 1:
        partnerACount += 6
        partnerBCount += 0



print('Partner A did an average of', format(partnerAAvg, ".2f"), 'years in prison')
print('Partner B did an average of', format(partnerBAvg, ".2f"), 'years in prison')
