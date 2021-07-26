"""Given an array of length N and an integer x, you need to find and return the last index of integer x present in the array. Return -1 if it is not present in the array.
Last index means - if x is present multiple times in the array, return the index at which x comes last in the array.
You should start traversing your array from 0, not from (N - 1).
Do this recursively. Indexing in the array starts from 0."""

from sys import setrecursionlimit
setrecursionlimit(11000)

def LastIndexOfNumber(arr, x):
    n = len(arr)

    if n <= 0:
        return -1
    if x == arr[n-1]:
        return arr[n-1]
    smallOutput = LastIndexOfNumber(arr[1:],x)

    if smallOutput != -1:
        return smallOutput + 1
    elif arr[0] == x:
        return 0
    else:
        return -1
        






arr = [int(x) for x in input().split()]
x = int(input())
print(LastIndexOfNumber(arr, x))
