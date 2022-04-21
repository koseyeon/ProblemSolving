import math
n = int(input())
res = int(n**0.5)
if res**2<n:
  print(res+1)
else:
  print(res)