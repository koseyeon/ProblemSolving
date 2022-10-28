m,n,k = map(int,input().split())
grid = [[0]*n for _ in range(m)]
for _ in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    for x in range(x1,x2):
        for y in range(y1,y2):
            grid[y][x] = -1
cnt = 0
area_list = []
dx = [0,1,0,-1]
dy = [1,0,-1,0]
for x in range(0,n):
    for y in range(0,m):
        if grid[y][x]!=0:
            continue
        cnt+=1
        area=1
        grid[y][x] = cnt
        stack = [[x,y]]
        while stack:
            [x,y] = stack.pop()
            for i in range(4):
                nx,ny = x+dx[i],y+dy[i]
                if(0<=nx<n and 0<=ny<m and grid[ny][nx]==0):
                    grid[ny][nx]=cnt
                    area+=1
                    stack.append([nx,ny])
        area_list.append(area)
print(cnt)
area_list.sort()
for area in area_list:
    print(area,end=" ")