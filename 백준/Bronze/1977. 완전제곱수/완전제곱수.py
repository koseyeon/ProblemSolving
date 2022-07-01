import math
m = int(input())
n = int(input())
first = False
f = 0
s = 0
for i in range(m,n+1):
    if i**0.5 == math.floor(i**0.5):
        if first == False:
            f = i
        first = True
        s += i
if first:
    print(s)
    print(f)
else:
    print(-1)