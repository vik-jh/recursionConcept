"""Write a recursive function that returns the sum of the digits of a given integer"""

from sys import setrecursionlimit
setrecursionlimit(11000)

def sumOfDigit(digit):
    if digit == 0:
        return 0 

    totalSum = sumOfDigit(digit//10) + (digit % 10)
    return totalSum


digit = int(input("Enter the digit whose sum you wish to find"))

print("Sum of digits: ", sumOfDigit(digit))


