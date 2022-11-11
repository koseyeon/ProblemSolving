import sys
from queue import PriorityQueue
input = sys.stdin.readline
q = PriorityQueue()
n = int(input())
def pop():
  if q.empty():
    print(0)
  else:
    print(q.get()[1])
def push(x):
  q.put([abs(x),x])
for _ in range(n):
  x = int(input())
  if x==0 : 
    pop()
  else:
    push(x)