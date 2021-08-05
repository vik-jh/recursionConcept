from sys import setrecursionlimit
setrecursionlimit(11000)


def stringToInteger(s):
    n = len(s)
    if n == 0:
        return 
    if n == 1:
        return int(s)

    small_int = int(s[0])
    integerValue = small_int * pow(10, n-1)
    recint = stringToInteger(s[1:])
    return integerValue + int(recint)
    


s = input("Enter the string of your choice \n")
ans = stringToInteger(s)
print(ans)