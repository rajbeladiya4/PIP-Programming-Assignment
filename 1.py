# You are given a string. Your task is to count the frequency of letters of the
# string and print the letters in descending order of frequency.If the following
# string is given as input to the program:
#
# aabbbccde
# Then, the output of the program should be:
#
# b 3
# a 2
# c 2
# d 1
# e 1
#
# 20CE003_RAJ BELADIYA
# https://github.com/rajbeladiya4/PIP-Programming-Assignment.git

# initializing string
string = "mississipi"

# for each element create dictionary
frequncyOfTheChar = {}

for i in string:
    if i in frequncyOfTheChar:
        frequncyOfTheChar[i] += 1
    else:
        frequncyOfTheChar[i] = 1

sortedFrequncyOfTheChar = dict(
    sorted(frequncyOfTheChar.items(), key=lambda x: x[1], reverse=True))

# printing result
print("Count of all characters in GeeksforGeeks is :\n " +
      str(sortedFrequncyOfTheChar))
