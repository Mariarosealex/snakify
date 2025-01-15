#H hours, M minutes and S seconds are passed since the midnight (0 ≤ H < 12, 0 ≤ M < 60, 0 ≤ S < 60). Determine the angle (in degrees) of the hour hand on the clock face right now.
h=int(input())
m=int(input())
s=int(input())
m=h*30+m*0.5+s*0.008333
print(m)
