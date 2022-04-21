grid = []
for _ in range(9):
  grid.append(list(input()))
candinate = [[[] for _ in range(9)] for _ in range(9)]
visited = [[0]*9 for _ in range(9)]
def possible(grid,i,j):
  candi = ['1','2','3','4','5','6','7','8','9']
  for x in range(9):
    if grid[x][j] in candi:
      candi.remove(grid[x][j])
    if grid[i][x] in candi:
      candi.remove(grid[i][x])
  for x in range((i//3)*3,(i//3)*3+3):
    for y in range((j//3)*3,(j//3)*3+3):
      if grid[x][y] in candi:
        candi.remove(grid[x][y])
  return sorted(candi,reverse=True)
prev = []
x,y = 0,0
stop = False
for i in range(9):
  for j in range(9):
    if grid[i][j]=='0':
      prev.append([i,j])
      x,y = i,j
      stop = True
      break
  if stop:
    break
def next(x,y):
  while True:
    if y == 8:
      x,y = x+1,0
    else:
      x,y = x,y+1
    if x>8 or grid[x][y]=='0':
      break
  return x,y
while x<=8 and y<=8:
  if grid[x][y]=='0':
    if visited[x][y]==0:
      candi = possible(grid,x,y)
      candinate[x][y]=candi
      visited[x][y]=1
    else:
      candi = candinate[x][y]
    if not candi:
      visited[x][y]=0
      x,y = prev.pop()
      grid[x][y]='0'
    else:
      grid[x][y]=candinate[x][y].pop()
      prev.append([x,y])
      x,y = next(x,y)
for g in grid:
  print(''.join(g))