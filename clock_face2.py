#Hour hand turned by α degrees since the midnight. Determine the angle by which minute hand turned since the start of the current hour. Input and output in this problems are floating-point numbers.
a=float(input('Enter the hour degree'))
n=a%30
q=n*12
print(q)
