#Given a positive real number, print its first digit to the right of the decimal point.
import math
n=float(input())
s=math.floor(n)
q=n-s
q=q*10
print(int(q))
