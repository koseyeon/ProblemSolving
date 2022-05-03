from collections import deque
n,m = map(int,input().split())
grid = []
for _ in range(n):
  grid.append(list(map(int,list(input()))))
d = deque([[0,0,0,1]])
dx = [0,1,0,-1]
dy = [1,0,-1,0]
INF = 10**10
answer = INF
visited = [[[0,0] for _ in range(m)] for _ in range(n)]
visited[0][0][0]=1
while d:
  x,y,w,cnt = d.popleft()
  if x==n-1 and y == m-1:
    answer = min(answer,cnt)
    continue
  for i in range(4):
    nx,ny = x+dx[i],y+dy[i]
    if 0<=nx<n and 0<=ny<m:
      if grid[nx][ny]==0 and w == 0 and visited[nx][ny][0]==0:
        visited[nx][ny][0]=1
        d.append([nx,ny,w,cnt+1])
      elif grid[nx][ny]==0 and w == 1 and visited[nx][ny][1]==0:
        visited[nx][ny][1]=1
        d.append([nx,ny,w,cnt+1])
      elif grid[nx][ny]==1 and w == 0 and visited[nx][ny][1]==0:
        visited[nx][ny][1]=1
        d.append([nx,ny,1,cnt+1])
if answer != INF:
  print(answer)
else:
  print(-1)