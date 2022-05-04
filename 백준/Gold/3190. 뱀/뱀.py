from collections import deque
n = int(input())
grid = [[0]*n for _ in range(n)]
k = int(input())
#apples =[]
for _ in range(k):
  a,b = map(int,input().split())
  grid[a-1][b-1]=1
rotation = {}
l = int(input())
for _ in range(l):
  a,b = input().split()
  rotation[int(a)] = b
def move(x,y,d):
  if d == 0: # 동쪽
    if 0<=x<n and 0<=y+1<n and grid[x][y+1]!=2: # 2는 뱀의 몸이 위치
      return x,y+1
  if d == 1: # 남쪽
    if 0<=x+1<n and 0<=y<n and grid[x+1][y]!=2: 
      return x+1,y
  if d == 2: # 서쪽
    if 0<=x<n and 0<=y-1<n and grid[x][y-1]!=2: 
      return x,y-1
  if d == 3: # 북쪽
    if 0<=x-1<n and 0<=y<n and grid[x-1][y]!=2: 
      return x-1,y
  return x,y
def rotate(time,d):
  if time in rotation.keys():
    if d == 0:
      if rotation[time] == 'L':
        return 3
      else:
        return 1
    if d == 1:
      if rotation[time] == 'L':
        return 0
      else:
        return 2
    if d == 2:
      if rotation[time] == 'L':
        return 1
      else:
        return 3
    if d == 3:
      if rotation[time] == 'L':
        return 2
      else:
        return 0
  else:
    return d
def eat(x,y):
  if grid[x][y]==1:
    return True
  else:
    return False
time = 0
x,y,d = 0,0,0 # 머리 좌표, 방향
history = deque([[0,0]]) # 지나간 좌표 목록
grid[x][y]=2
while True:
  d = rotate(time,d)
  nx,ny = move(x,y,d)
  if [x,y] == [nx, ny]:
    break
  else:
    x,y = nx,ny
    history.append([x,y])
  if eat(x,y):
    grid[x][y]=2
  else:
    grid[x][y]=2
    tx,ty = history.popleft()
    grid[tx][ty]=0
  time+=1
print(time+1)