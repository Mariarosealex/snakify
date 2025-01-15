#chess king moves horizontally, vertically or diagonally to any adjacent cell. Given two different cells of the chessboard, determine whether a king can go from the first cell to the second in one move.
x=int(input())
y=int(input())
a=int(input())
b=int(input())
if (x==a or x==a+1 or x==a-1)and (y==b or y==b+1 or y==b-1):
    print('YES')
else:
    print('NO')
