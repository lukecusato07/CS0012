# Lists
nums = [1,2,3,4,5]

halloween_party = ["John", "Jane", "Prof. DeNardis"]

print(nums[1:4])

# .pop() --> take off the end of the list
halloween_party.pop()

print(halloween_party)

# .append() --> add on to the list
halloween_party.append("Prof. DeNardis")

halloween_party[2] = "Luke"
print(halloween_party)

halloween_parties = [["John", "Jane", "Prof. DeNardis"], ["a","b","c"], ["x","y","z"]]

num_of_parties = 20

# THIS IS HOW YOU WILL MAKE A LIST OF LISTS IN THE LAB
halloween_parties = [[] for _ in range(num_of_parties)]
print(halloween_parties)


# Dictionaries
# Format --> {key0:value0, key1:value1, key2:value2}
party_rsvp = {"Luke":4124124124, "Prof":5125125125, "Dracula":6466466}

# Access values in a dictionary
print(party_rsvp["Dracula"])

# .items() --> [("Luke",4124124124), ("Prof",5125125125), ("Dracula":6466466)]
partier_count = 0
for name, number in party_rsvp.items():
    partier_count += 1
    #print(name, number)
    print("Parter:", partier_count, "\nParter name:", name, "\nPartier Number:", number)


# Keyword del
del party_rsvp["Prof"]
print(party_rsvp)


nums = [1,1,1,2,2,4,5,5,5,5,6,7]

# WE ARE NTOT USING COUNTER IN THE LAB, JUST AN EXAMPLE
from collections import Counter
nums_dict = Counter(nums)

print(nums_dict)
nums = [1,1,2,2,2,2,3]

freq_check = {}

for num in nums:
    if num not in freq_check:
        # Key             Value
        freq_check[num] = 1
    elif num in freq_check:
        freq_check[num] += 1
print(freq_check)


# Ex.) http://www.nytimes.com/2016/04/18/nyregion/spare-a-swipe-new-york-city-eases-rules-for-a-subway-request.html
# Arg is whatever line I found that has a url

def get_week(URL):
    # All articles are from 2016
    # Splitting up URL to find the date
    split_URL = URL.split("/")

    # Getting the month and day from the URL
    month = int(split_URL[4])
    day = int(split_URL[5])

    # Keep track of how many days in the year have passed
    april = 90
    may = 120
    june = 151

    # Keep track of curr num of days
    num_days = 0

    if month == 4:
        num_days = april + day

    elif month == 5:
        num_days = may + day

    elif month == 6:
        num_days = june + day


    # We know we are at 4/18
    april15th = 105

    # I'm on 157
    num_days -= april15th
    # Published 52 days after the first article

    week_num = num_days // 7


    # Need to return something from this function
        # **HINT** What is something in this function that can help us out with our prev functions
    # return


def process_file(f_name):
    weekly_words = [[] for _ in range(11)]
    word_freq = [{} for _ in range(11)]
    nums = [1,1,2,2,2,2,3]

    freq_check = {}

    for num in nums:
        if num not in freq_check:
            # Key             Value
            freq_check[num] = 1
        elif num in freq_check:
            freq_check[num] += 1





    # I need to make a var for some num that is an invalid week
        # **HINT** why did we init article count to 0?
    # curr_week = ???

    for line in open_file:
        # curr_week.append("Breaking")
        # curr_week.append("News")
        weekly_words[curr_week].append("Breaking News!")


    return weekly_words




URL = "http://www.nytimes.com/2016/04/18/nyregion/spare-a-swipe-new-york-city-eases-rules-for-a-subway-request.html"
split_URL = URL.split("/")

month = int(split_URL[4])
day = int(split_URL[5])

print("Today's date:", month, "/", day)
