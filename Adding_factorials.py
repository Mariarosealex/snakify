#Given an integer n, print the sum 1!+2!+3!+...+n!.This problem has a solution with only one loop, so try to discover it. And don't use the math library :)
a=int(input())
sum=0
fact=1
for i in range(1,a+1):
    fact*=i
    sum+=fact
print(sum)
