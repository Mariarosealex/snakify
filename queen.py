#Chess queen moves horizontally, vertically or diagonally to any number of cells. Given two different cells of the chessboard, determine whether a queen can go from the first cell to the second in one move.
x=int(input())
y=int(input())
a=int(input())
b=int(input())
if x==a or y==b or abs(x-a)==abs(y-b):
    print('YES')
else:
    print('NO')
