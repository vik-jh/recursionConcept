def staircase(n):
    if n==1:
        return 1
    if n==2:
        return 2
    if n==3:
        return 4
    x=staircase(n-1)
    y=staircase(n-2)
    z=staircase(n-3)
    possible_ways=x+y+z
    return possible_ways


n=int(input())
#step=int(input())
x=staircase(n)
print(x)
