import sys
input = sys.stdin.readline
A = [0]
m = int(input())
t = 0
s = 0
for _ in range(m):
  q = list(map(int,input().split()))
  if len(q)==2:
    a,x = q
    if a == 1:
      s += x
      t ^= x
    elif a == 2:
      s -= x
      t ^= x  
  elif len(q)==1:
    a = q[0]
    if a == 3:
      print(s)
    elif a == 4:
      print(t)