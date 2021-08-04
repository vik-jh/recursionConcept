"""Given k, find the geometric sum i.e.
1 + 1/2 + 1/4 + 1/8 + ... + 1/(2^k) 
using recursion."""

def geometricSum(k, sum):
    if k == 0:
        return 1
    
    TotalSum = (1/2**k) + geometricSum(k-1, sum)
    return TotalSum 






k = int(input())
ans = geometricSum(k, sum)
print(ans)