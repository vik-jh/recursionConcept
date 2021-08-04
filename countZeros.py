"""Given an integer N, count and return the number of zeros that are present in the given integer using recursion."""

def countZero(n):
    if n <10:
        if n == 0:
            return 1
        else:
            return 0

    if n % 10 == 0:
        return 1 + countZero(n//10)

    else:
        return countZero(n//10)


n = int(input("Eneter the number: \n"))

print("Total number of zeros: \n \t", countZero(n))
