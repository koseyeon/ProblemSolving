n,m = map(int,input().split())
r,c,d = map(int,input().split())
grid = []
for i in range(n):
  grid.append(list(map(int,input().split())))
def next_direction(d):
  if d == 0:
    return 3
  else:
    return d-1
def next_pos(r,c,d):
  if d == 0:
    if 0<=r-1<n and 0<=c<m and grid[r-1][c]==0:
      return [r-1,c]
    else:
      return [r,c]
  if d == 1:
    if 0<=r<n and 0<=c+1<m and grid[r][c+1]==0:
      return [r,c+1]
    else:
      return [r,c]
  if d == 2:
    if 0<=r+1<n and 0<=c<m and grid[r+1][c]==0:
      return [r+1,c]
    else:
      return [r,c]
  if d == 3:
    if 0<=r<n and 0<=c-1<m and grid[r][c-1]==0:
      return [r,c-1]
    else:
      return [r,c]
def find_back(r,c,d):
  if d == 0:
    if 0<=r+1<n and 0<=c<m and grid[r+1][c]==2:
      return [r+1,c]
    else:
      return [r,c]
  if d == 1:
    if 0<=r<n and 0<=c-1<m and grid[r][c-1]==2:
      return [r,c-1]
    else:
      return [r,c]
  if d == 2:
    if 0<=r-1<n and 0<=c<m and grid[r-1][c]==2:
      return [r-1,c]
    else:
      return [r,c]
  if d == 3:
    if 0<=r<n and 0<=c+1<m and grid[r][c+1]==2:
      return [r,c+1]
    else:
      return [r,c]
answer = 1
d_cnt = 0
while True:
  grid[r][c] = 2
  d = next_direction(d)
  d_cnt+=1
  [nr,nc] = next_pos(r,c,d)
  if [r,c] == [nr,nc]:
    if d_cnt == 4:
      if [r,c] == find_back(r,c,d):
        break
      else:
        r,c = find_back(r,c,d)
        d_cnt = 0
  else:
    r,c = nr,nc
    d_cnt = 0
    answer+=1
print(answer)