#A car can cover distance of N kilometers per day. How many days will it take to cover a route of length M kilometers? The program gets two numbers: N and M.
import math
n=float(input())
m=float(input())
print(math.ceil(m/n))
