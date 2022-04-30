n = int(input())
grid = []
for _ in range(n):
  grid.append(list(input()))
dx = [0,1,0,-1]
dy = [1,0,-1,0]
cnt = 0
visited1 = [[0]*n for _ in range(n)]
for i in range(n):
  for j in range(n):
    if visited1[i][j]==0:
      visited1[i][j]=1
      s = [[i,j]]
      color = grid[i][j]
      cnt += 1 
      while s:
        x,y = s.pop()
        for k in range(4):
          nx,ny = x+dx[k],y+dy[k]
          if 0<=nx<n and 0<=ny<n and visited1[nx][ny]==0 and grid[nx][ny]==color:
            visited1[nx][ny]=1
            s.append([nx,ny])
visited2 = [[0]*n for _ in range(n)]
cnt2 = 0
for i in range(n):
  for j in range(n):
    if visited2[i][j]==0:
      visited2[i][j]=1
      s = [[i,j]]
      if grid[i][j]=="R" or grid[i][j]=="G":
        color = ["R","G"]
      else:
        color = ["B"]
      cnt2 += 1 
      while s:
        x,y = s.pop()
        for k in range(4):
          nx,ny = x+dx[k],y+dy[k]
          if 0<=nx<n and 0<=ny<n and visited2[nx][ny]==0 and grid[nx][ny] in color:
            visited2[nx][ny]=1
            s.append([nx,ny])
print(cnt,cnt2)