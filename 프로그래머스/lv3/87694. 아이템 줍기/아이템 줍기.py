from collections import deque
def isInRect(x,y,rectangle):
    for rect in rectangle:
        x1,y1,x2,y2 = rect
        if x1<=x<=x2 and y1<=y<=y2:
            return True
    return False
def findBoundary(rectangle):
    grid = [[0]*102 for _ in range(102)]
    dx = [0,1,0,-1,1,-1,1,-1]
    dy = [1,0,-1,0,1,-1,-1,1]
    for i in range(102):
        for j in range(102):
            if grid[i][j] == 0 and not isInRect(i,j,rectangle):
                grid[i][j] = 1
                stack = [[i,j]]
                while stack:
                    x,y = stack.pop()
                    for k in range(8):
                        nx,ny = x+dx[k],y+dy[k]
                        if 0<=nx<102 and 0<=ny<102 and grid[nx][ny] == 0:
                            if isInRect(nx,ny,rectangle):
                                grid[nx][ny] = "#"
                            else:
                                grid[nx][ny] = 1
                                stack.append([nx,ny])
    return grid
def findMinDist(grid,characterX, characterY, itemX, itemY):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    d = deque([[characterX, characterY,0]])
    while d:
        x,y,cnt = d.popleft()
        if x == itemX and y == itemY:
            return cnt//2
        for k in range(4):
            nx,ny = x+dx[k],y+dy[k]
            if 0<=nx<102 and 0<=ny<102 and grid[nx][ny] == "#":
                grid[nx][ny] = "*"
                d.append([nx,ny,cnt+1])
def solution(rectangle, characterX, characterY, itemX, itemY):
    new_rectangle = []
    for rect in rectangle:
      x1,y1,x2,y2 = rect
      new_rectangle.append([x1*2,y1*2,x2*2,y2*2])
    grid = findBoundary(new_rectangle)
    return findMinDist(grid,characterX*2, characterY*2, itemX*2, itemY*2)