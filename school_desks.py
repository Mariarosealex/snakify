#A school decided to replace the desks in three classrooms. Each desk sits two students. Given the number of students in each class, print the smallest possible number of desks that can be purchased.
a=int(input())
b=int(input())
c=int(input())
d=a//2+b//2+c//2
if(a%2==1):
    d=d+1;
if(b%2==1):
    d=d+1;
if(c%2==1):
    d=d+1;
print(d)
