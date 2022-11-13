import sys
input = sys.stdin.readline
n = int(input())
grid = [[0]*100 for _ in range(100)]
for _ in range(n):
  l,d = map(int,input().split())
  for i in range(l,l+10):
    for j in range(d,d+10):
      grid[i][j]=1
ans = 0
for i in range(100):
  for j in range(100):
    if grid[i][j] == 1:
      ans += 1
print(ans)