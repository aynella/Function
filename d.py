from math import sqrt
def IsPointInSquare(x, y):
    if(abs(x)+abs(y)<=1):
    #if(sqrt(x**2+y**2)<=1):
        return "YES"
    else:
        return "NO"
x=float(input())
y=float(input())
print(IsPointInSquare(x, y))
