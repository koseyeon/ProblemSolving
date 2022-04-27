n = int(input())
INF = 10**9
grid = [[INF]*n for _ in range(n)]
for i in range(n):
  l = list(map(int,input().split()))
  for j in range(n):
    if l[j]==1:
      grid[i][j]=1
for k in range(n):
  for i in range(n):
    for j in range(n):
      grid[i][j] = min(grid[i][j],grid[i][k]+grid[k][j])
for i in range(n):
  for j in range(n):
    if grid[i][j]==INF:
      grid[i][j]=0
    else:
      grid[i][j]=1
for g in grid:
  print(*g)