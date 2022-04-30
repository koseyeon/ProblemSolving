from collections import deque
m,n,h = map(int,input().split())
grid = []
for _ in range(h):
  g = []
  for _ in range(n):
    g.append(list(map(int,input().split())))
  grid.append(g)
dx = [0,1,0,-1,0,0]
dy = [1,0,-1,0,0,0]
dz = [0,0,0,0,1,-1]
init = []
for i in range(h):
  for j in range(n):
    for k in range(m):
      if grid[i][j][k]==1:
        init.append([j,k,i,1])
d = deque(init)
result = 0
while d:
  x,y,z,cnt = d.popleft()
  for w in range(6):
    nx,ny,nz = x+dx[w],y+dy[w],z+dz[w]
    if 0<=nx<n and 0<=ny<m and 0<=nz<h and grid[nz][nx][ny]==0:
      grid[nz][nx][ny]=cnt
      result = max(result,cnt)
      d.append([nx,ny,nz,cnt+1])
for i in range(h):
  for j in range(n):
    for k in range(m):
      if grid[i][j][k]==0:
        result = -1
print(result)