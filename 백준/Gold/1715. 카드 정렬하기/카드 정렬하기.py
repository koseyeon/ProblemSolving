import sys
from queue import PriorityQueue
input = sys.stdin.readline
n = int(input())
q = PriorityQueue()
for _ in range(n):
  q.put(int(input()))
ans = 0
if n == 1:
  print(0)
else:
  while q.qsize()>=2:
    a = q.get()
    b = q.get()
    ans += a+b
    q.put(a+b)
  print(ans)
