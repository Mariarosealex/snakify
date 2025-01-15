#Given the integer N - the number of minutes that is passed since midnight - how many hours and minutes are displayed on the 24h digital clock?
import math
n=int(input())
print(str(n//60)+' '+str(n%60))
