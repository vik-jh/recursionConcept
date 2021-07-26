"""Given an array of length N and an integer x, you need to find and return the first index of integer x present in the array. Return -1 if it is not present in the array.
First index means, the index of first occurrence of x in the input array.
Do this recursively. Indexing in the array starts from 0."""
from sys import setrecursionlimit
setrecursionlimit(11000)


def FirstIndexOfNumber(arr, X):

    n = len(arr)

    if n <= 0:
        return -1

    if X == arr[0]:
        return 0

    smallAns = FirstIndexOfNumber(arr[1:],X)
    if smallAns == -1:
        return -1

    else:
        return smallAns + 1

    








arr = [int(y) for y in input().split()]
X = int(input())
print(FirstIndexOfNumber(arr, X))




