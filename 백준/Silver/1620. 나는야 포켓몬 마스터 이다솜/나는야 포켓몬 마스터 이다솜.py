import sys
input = sys.stdin.readline
m, n = map(int,input().split())
d1 = {}
d2 = {}
for i in range(1,m+1):
  name = input().rstrip()
  d1[i] = name
  d2[name] = i
for i in range(1,n+1):
  q = input().rstrip()
  if q.isdigit():
    print(d1[int(q)])
  else:
    print(d2[q])