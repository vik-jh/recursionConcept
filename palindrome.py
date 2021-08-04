"""Check whether a given String S is a palindrome using recursion. Return true or false.
Input Format :
String S
Output Format :
'true' or 'false'"""

def checkPalindrome(S):
    n = len(S)
    if n == 0 or n == 1:
        return True
    if S[0] != S[n-1]:
        return False

    return checkPalindrome(S[1:n-1])




S = input()

if checkPalindrome(S):
    print("True")
else:
    print("False")