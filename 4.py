# Given a list of integers, write a program to print the count of all possible unique
# combinations of numbers whose sum is equal to K.
# Input
# The first line of input will contai n space-separated integers.
# The second line of input will contain an integer, denoting K.
#
# Output
# The output should be containing the count of all unique combinati ons of numbers
# whose sum is equal to K.
# Sample Input 1
# 2 4 6 1 3
# 6
# Sample Output 1
# 3
#
# 20CE003_RAJ BELADIYA
# https://github.com/rajbeladiya4/PIP-Programming-Assignment.git

from itertools import combinations

# Get a list of numbers from input
numbers = [int(n) for n in input().split()]

# Get K value from input
k = int(input())

# Count combinations that sum to K
count = 0

# Try combinations of all possible sizes
for i in range(1, len(numbers)+1):
    # Try all combinations of size i
    for c in combinations(numbers, i):
        # If this combination sums to K, then increase the count
        if sum(c) == k:
            count += 1
            
print(count)
