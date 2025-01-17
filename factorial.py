#In mathematics, the factorial of an integer n, denoted by n! is the following product:n!=1×2×…×nFor the given integer n calculate the value n!. Don't use math module in this exercise.

fact=1
for i in range(1,int(input())+1):
    fact*=i
print(fact)
