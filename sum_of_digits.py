#Given a three-digit number. Find the sum of its digits.
n=int(input())
a=n//100
c=n%10
b=n//10-a*10
print(a+b+c)
