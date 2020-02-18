import math
def IsPointInSquare(x, y):
    if(abs(x)<=1 and abs(y)<=1):
        return "YES"
    else:
        return "NO"

x=float(input())
y=float(input())
print(IsPointInSquare(x, y))