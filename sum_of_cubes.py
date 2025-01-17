#For the given integer N calculate the following sum:13+23+…+N3
a=int(input())
cube=0
for i in range(1,a+1):
    cube=cube+(i**3)
print(cube)
