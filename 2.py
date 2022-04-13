# Write a procedure to find min, max, mean, standard deviation, variance of number
# list.Example
#
# Input: 10 50 80 70 49 23 11 4
# output: 4 80 37.13 27.25 848.70
#
# 20CE003_RAJ BELADIYA
# https://github.com/rajbeladiya4/PIP-Programming-Assignment.git

from re import A
import statistics
import pandas as pd

list = pd.Series([10, 50, 80, 70, 49, 23, 11, 4])

# inbuilt Functions to find the mean median and mode
mean = list.mean()
median = list.median()
mode = list.mode()

print(list.min())       # min() to find the minimum element
print(list.max())       # max() to find the maximum element
print(mean)
print(median)
print(mode)
print("Variance of sample set is % s" % (statistics.variance(list)))
