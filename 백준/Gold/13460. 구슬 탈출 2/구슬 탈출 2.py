def up(x,y,tx,ty):
  nx,ny = 0,0
  for i in range(x-1,-1,-1):
    if grid[i][y]=='#' or (i==tx and y ==ty):
      nx,ny=i+1,y
      break
    elif grid[i][y]=='O':
      nx,ny=0,0
      break
  return [nx,ny]
def down(x,y,tx,ty):
  nx,ny = 0,0
  for i in range(x+1,n):
    if grid[i][y]=='#' or (i==tx and y ==ty):
      nx,ny=i-1,y
      break
    elif grid[i][y]=='O':
      nx,ny=0,0
      break
  return [nx,ny]
def right(x,y,tx,ty):
  nx,ny = 0,0
  for i in range(y+1,m):
    if grid[x][i]=='#' or (i==ty and x ==tx):
      nx,ny=x,i-1
      break
    elif grid[x][i]=='O':
      nx,ny=0,0
      break
  return [nx,ny]
def left(x,y,tx,ty):
  nx,ny = 0,0
  for i in range(y-1,-1,-1):
    if grid[x][i]=='#' or (i==ty and x ==tx):
      nx,ny=x,i+1
      break
    elif grid[x][i]=='O':
      nx,ny=0,0
      break
  return [nx,ny]
def enter(x,y):
  if x == 0 and y == 0:
    return True
  else:
    return False
n,m = map(int,input().split())
grid = []
rx,ry = 0,0
bx,by = 0,0
MAX = 10**9
ans = MAX
for i in range(n):
  l = list(input())
  grid.append(l)
  for j in range(m):
    if l[j]=='R':
      rx,ry = i,j
      grid[rx][ry]='.'
    elif l[j]=='B':
      bx,by = i,j
      grid[bx][by]='.'
s = [[rx,ry,bx,by,0]]
while s:
  rx,ry,bx,by,cnt = s.pop()
  if cnt<=10 and enter(rx,ry) and not enter(bx,by):
    ans = min(ans,cnt)
    continue
  elif cnt>10:
    continue
  if rx>bx:
    nbx,nby = up(bx,by,rx,ry)
    nrx,nry = up(rx,ry,nbx,nby)
  else:
    nrx,nry = up(rx,ry,bx,by)
    nbx,nby = up(bx,by,nrx,nry)
  s.append([nrx,nry,nbx,nby,cnt+1])
  if rx>bx:
    nrx,nry = down(rx,ry,bx,by)
    nbx,nby = down(bx,by,nrx,nry)
  else:
    nbx,nby = down(bx,by,rx,ry)
    nrx,nry = down(rx,ry,nbx,nby)
  s.append([nrx,nry,nbx,nby,cnt+1])
  if ry>by:
    nrx,nry = right(rx,ry,bx,by)
    nbx,nby = right(bx,by,nrx,nry)
  else:
    nbx,nby = right(bx,by,rx,ry)
    nrx,nry = right(rx,ry,nbx,nby)
  s.append([nrx,nry,nbx,nby,cnt+1])
  if ry>by:
    nbx,nby = left(bx,by,rx,ry)
    nrx,nry = left(rx,ry,nbx,nby)
  else:
    nrx,nry = left(rx,ry,bx,by)
    nbx,nby = left(bx,by,nrx,nry)
  s.append([nrx,nry,nbx,nby,cnt+1])
if ans == MAX:
  print(-1)
else:
  print(ans)