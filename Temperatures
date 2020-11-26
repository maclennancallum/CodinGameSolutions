import sys
import math

# Temperatures solution - Callum MacLennan 
# 26/11/2020

# n - Number of temperatures 
n = int(input())  
# temps - list of temperatures
temps = input()
# Generates an array containing the temperatures 
tempArr = temps.split(' ')

# Generates an initial min temp 
# if n equals zero the temp is set to zero 
if n == 0:
    lowestNum = int(0)
else: 
    lowestNum = int(5526)

# for loop to determine the lowest temperature in the array 
i = 0 
for i in range(n):
    # stores each individual temperature as temporary variable x
    x = int(tempArr[i])
    # If x is smaller than the previous minimum it becomes the new minimum
    if abs(x) < abs(lowestNum):
        lowestNum = x
    elif abs(x) == abs(lowestNum):
        lowestNum = abs(x)
    
# outputs the final minimum temperature         
print(lowestNum)
    
