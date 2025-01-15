#Given two cells of a chessboard. If they are painted in one color, print the word YES, and if in a different color - NO.
x=int(input())
y=int(input())
a=int(input())
b=int(input())
if (x+y)%2==(a+b)%2:
    print('YES')
else:
    print('NO')
