import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
m,n = map(int,input().split())
grid = []
for _ in range(m):
  grid.append(list(map(int,input().split())))
dx = [0,1,0,-1]
dy = [1,0,-1,0]
visited = [[-1]*n for _ in range(m)]
def dfs(x,y):
  if x == m-1 and y == n-1:
    return 1
  if visited[x][y]==-1:
    visited[x][y]=0
  else:
    return visited[x][y]
  for i in range(4):
    nx,ny = x+dx[i],y+dy[i]
    if 0<=nx<m and 0<=ny<n and grid[nx][ny]<grid[x][y]:
      visited[x][y]+=dfs(nx,ny)
  return visited[x][y]
print(dfs(0,0))