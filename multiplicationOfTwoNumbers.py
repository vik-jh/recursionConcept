"""Given two integers M & N, calculate and return their multiplication using recursion. You can only use subtraction and addition for your calculation. No other operators are allowed.
Input format :
Line 1 : Integer M
Line 2 : Integer N
Output format :
M x N
Constraints :
0 <= M <= 1000
0 <= N <= 1000
Sample Input 1 :
3 
5
Sample Output 1 :
15"""

def multiple(n, m):
    if m == 0:
        return 0
    n = n + multiple(n, m-1)
    return n

    

    

n = int(input("Enter the 1st number for multiplication"))
m = int(input("Enter the 2nd number for multiplication"))

print("Multiple of two given number:", multiple(n, m))




