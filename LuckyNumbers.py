import sys
import math

# Lucky Numbers - Callum MacLennan
# 26/11/2020
l, r = [int(i) for i in input().split()]

# Variables used in the for loop 
six = str(6)
eight = str(8)
luckyNum = 0 
i = l

# loops for every number between l and r 
while l <= r:
    num = str(l)
    # if the number contains 6 or 8, one is added to the counter 
    if six in num or eight in num:
        luckyNum = luckyNum + 1
    # if the number contains both 6 and 8, one is removed from the counter
    if six in num and eight in num:
        luckyNum = luckyNum - 1 
    l = l + 1
# Prints the final value of lucky numbers 
print(luckyNum)
