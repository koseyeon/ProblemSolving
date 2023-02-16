from collections import deque
def solution(maps):
    answer = 0
    n,m = len(maps),len(maps[0])
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    maps[0][0] = 0
    d = deque([[0,0,1]])
    while d:
        x,y,cnt = d.popleft()
        if x == n-1 and y == m-1:
            return cnt
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and maps[nx][ny] == 1:
                maps[nx][ny] = 0
                d.append([nx,ny,cnt+1])
    return -1