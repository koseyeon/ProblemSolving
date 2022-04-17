n = int(input())
map_ = []
for _ in range(n):
  l = list(map(int,input().split()))
  map_.append(l)
dx = [0,1,0,-1]
dy = [1,0,-1,0]
def cango(x,y,rain,visited):
  if 0<=x<n and 0<=y<n and visited[x][y]==0 and map_[x][y]>rain:
    return True
  else:
    return False
def dfs(rain):
  visited = [[0]*n for _ in range(n)]
  cnt = 0
  for x in range(n):
    for y in range(n):
      if map_[x][y]>rain and visited[x][y]==0:
        s = [[x,y]]
        visited[x][y]=1
        while s:
          px,py = s.pop()
          for i in range(4):
            nx,ny = px+dx[i],py+dy[i]
            if cango(nx,ny,rain,visited):
              s.append([nx,ny])
              visited[nx][ny]=1
        cnt += 1
  return cnt
ans = 0
for rain in range(0,101):
  ans = max(ans,dfs(rain))
print(ans)
