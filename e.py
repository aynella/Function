from math import sqrt
def IsPointInCircle (x, y, xc, yc, r):
    if sqrt ((xc-x)**2+(yc-y)**2<=r**2):
        return "YES"
    else:
        return "NO"
 
x=float(input())
y=float(input())
xc=float(input())
yc=float(input())
r=float(input())
print(IsPointInCircle(x, y, xc, yc, r))