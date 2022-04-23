def cango(x,y,s):
  if 0<=x<r and 0<=y<c and not (s & 1<<ord(grid[x][y])-65):
    return True
  return False
def dfs(x,y,state,cnt):
  global ans
  s = [[x,y,state,cnt]]
  while s:
    x,y,state,cnt = s.pop()
    ans = max(ans,cnt)
    for i in range(4):
      nx,ny = x+dx[i],y+dy[i]
      if cango(nx,ny,state):
        ns = state | (1<<ord(grid[nx][ny])-65)
        s.append([nx,ny,ns,cnt+1])
r,c = map(int,input().split())
grid = []
for _ in range(r):
  grid.append(list(input()))
ans = 0
dx = [0,1,0,-1]
dy = [1,0,-1,0]
dfs(0,0,1<<(ord(grid[0][0])-65),1)
print(ans)