#In chess, the bishop moves diagonally, any number of squares. Given two different squares of the chessboard, determine whether a bishop can go from the first to the second in one move.
x=int(input())
y=int(input())
a=int(input())
b=int(input())
if ((x+y)-(a+b))==0:
    print('YES')

elif ( x==y and b==a):
    print('YES')
else:
    print('NO')
