import math
n,k = map(int,input().split())
a = 0
b = 1
while True:
    if k - 9*(10**a)*b >0:
        k -= 9*(10**a)*b
    else:
        break
    a+=1
    b+=1
c = math.ceil(k/b)
d = (k-1)%b
result = c
while a!=0:
    result += 9*(10**(a-1))
    a-=1
result = str(result)
if n < int(result):
    print(-1)
else:
    print(result[d])