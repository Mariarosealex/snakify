#Chess rook moves horizontally or vertically. Given two different cells of the chessboard, determine whether a rook can go from the first cell to the second in one move.
x=int(input('Current x cordinate'))
y=int(input('Current y cordinate'))
a=int(input('new x cordinate'))
b=int(input('new y cordinate'))
if (a==x+1 and b==y-1) or(a==x-1 and b==y+1):
    print('NO')
elif (a==b==x) or (a==b==y) or (a==x==y) or (b==y==x):
    print('YES')
elif (a==x+2 and b==y-2) or (a==x-2 and b==y+2):
    print('NO')
elif a==b:
    print('NO')
elif a==x and b==y+1 or b==y+2 or b==y-1 or b==y-2:
    print('YES')
elif b==y and a==y+1 or a==y-1:
    print('YES')
elif a==x+1 and b==y+1:
    print('NO')
else:
    print('NO')
