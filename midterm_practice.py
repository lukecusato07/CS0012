# Structure of a function
# For this function that I am defining(given these arguments):
    # Do this

# def function_name(arguments):
    # do this

# Write a main function since that is what the computer is concerned about
# def main():
    # function1(argument1)
    # function2(argument2)

# call main (tell the computer to do this ^)
# main()


def squared(my_num):
    # We want this function to square the argument and print it
    my_num = my_num**2
    print("The squared value of your argument is:", my_num)
    print("\n")


# Unindent to make a new function
def your_name():
    my_str = input("What's your name?: ")
    print(my_str.upper())
    print("\n")




def happy_bday():
    # Example input is "June 4th" or "06/04" etc.
    yourBDay = input("When is your birthday?: ")
    print("Wishing you a happy birthday on,", yourBDay+"!")
    print("\n")



# What the program is concerned with goes here
def main():
    squared(40)
    squared(205)

    your_name()
    happy_bday()



main()
