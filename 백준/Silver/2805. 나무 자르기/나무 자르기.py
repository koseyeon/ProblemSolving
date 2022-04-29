import sys
input = sys.stdin.readline
import bisect
n,m = map(int,input().split())
trees = list(map(int,input().split()))
start = 0
end = 2000000000
def calculate(x):
  s = 0
  for i in range(n):
    if trees[i]>x:
      s+=trees[i]-x
  return s
while start <= end:
  mid  = (start + end)//2
  c = calculate(mid)
  if c == m:
    break
  elif c > m:
    start = mid + 1
  else:
    end = mid - 1
if c == m:
  print(mid)
else:
  print(start-1)