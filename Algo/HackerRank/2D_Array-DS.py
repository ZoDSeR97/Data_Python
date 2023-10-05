# Given a 6x6 2D array A
# An hourglass in A is a subset of values with indices falling in this pattern in array's graphical representation:
# a b c
#   d
# e f g
# here are 16 hourglasses in the array. An hourglass sum is the sum of an hourglass' values. 
# Calculate the hourglass sum for every hourglass in array, then print the maximum hourglass sum. 
#
# Constraints: 
# The array will always be 6x6
# -9 <= array[row][col] <= 9
# 0 <= row, col <= 5

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    maxSum = -63 # base on the contraints: -63 is the lowest value an hourglass can have
    for row in range(4):
        for col in range(4):
            sumMatrix = sum(arr[row][col:col+3]) + sum(arr[row+2][col:col+3]) + arr[row+1][col+1]
            maxSum = max(sumMatrix, maxSum)
    return maxSum   

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    print(result)