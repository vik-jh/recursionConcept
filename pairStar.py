from sys import setrecursionlimit
setrecursionlimit(11000)

def pairString(s):
    n = len(s)
    if n == 1:
        return s

    if s[0] == s[1]:
        return s[0] + "*" + pairString(s[1:])
    else:
        return s[0] + pairString(s[1:])

    





s = input("Enter the value of String \n")
ans = pairString(s)
print(ans)