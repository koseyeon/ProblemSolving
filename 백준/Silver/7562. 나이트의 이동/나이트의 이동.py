from collections import deque
def next_points(x,y):
    candinate = [[x+1,y+2],[x+1,y-2],[x+2,y+1],[x+2,y-1],[x-1,y-2],[x-1,y+2],[x-2,y-1],[x-2,y+1]]
    next = []
    for cx,cy in candinate:
      if 0<=cx<n and 0<=cy<n and visited[cx][cy]==0:
        next.append([cx,cy])
    return next
t = int(input())
for _ in range(t):
  n = int(input())
  x,y = map(int,input().split())
  tx,ty = map(int,input().split())
  grid = [[0]*n for _ in range(n)]
  visited = [[0]*n for _ in range(n)]
  d = deque([[x,y,0]])
  ans = 0
  while d:
    x,y,cnt = d.popleft()
    if x == tx and y == ty: 
      ans = cnt
      break
    for nx,ny in next_points(x,y):
      visited[nx][ny]=1
      d.append([nx,ny,cnt+1])
  print(ans)