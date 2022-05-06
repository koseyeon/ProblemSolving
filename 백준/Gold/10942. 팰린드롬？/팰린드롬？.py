import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int,input().split()))
pd = [[0]*n for _ in range(n)]
def find_pd1(i):
  s,e = i,i
  while 0<=s and e<=n-1:
    if nums[s] == nums[e]:
      pd[s][e]=1
    else:
      break
    s -= 1
    e += 1
def find_pd2(i):
  s,e = i,i+1
  while 0<=s and e<=n-1:
    if nums[s] == nums[e]:
      pd[s][e]=1
    else:
      break
    s -= 1
    e += 1
for i in range(n):
  find_pd1(i)
for i in range(n-1):
  find_pd2(i)
m = int(input())
for _ in range(m):
  s,e = map(int,input().split())
  print(pd[s-1][e-1])
