dx = [0,1,0,-1,1,-1,1,-1]
dy = [1,0,-1,0,1,1,-1,-1]
while True:
  w,h = map(int,input().split())
  if w==h==0:
    break
  map_ =[]
  for _ in range(h):
    map_.append(list(map(int,input().split())))
  visited = [[0]*w for _ in range(h)]
  cnt = 0
  for i in range(h):
    for j in range(w):
      if map_[i][j]==0 or visited[i][j]==1:
        continue
      s = [[i,j]]
      visited[i][j]=1
      while s:
        x,y = s.pop()
        for k in range(8):
          nx,ny = x+dx[k],y+dy[k]
          if 0<=nx<h and 0<=ny<w and map_[nx][ny]==1 and visited[nx][ny]==0:
            s.append([nx,ny])
            visited[nx][ny]=1
      cnt+=1
  print(cnt)