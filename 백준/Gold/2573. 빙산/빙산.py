import sys
input = sys.stdin.readline
N,M = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]

dx = [0,1,-1,0]
dy = [1,0,0,-1]

def adj_water(x,y):
    cnt = 0
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<N and 0<=ny<M and grid[nx][ny] == 0:
            cnt += 1
    return cnt

year = 0

search_list = []
for i in range(N):
    for j in range(M):
        if grid[i][j] > 0:
            search_list.append([i,j])

while True:
    year += 1
    new_grid = [[0]*M for _ in range(N)]
    new_search_list = []
    for i,j in search_list:
        if grid[i][j] > 0:
            new_grid[i][j] = max(0,grid[i][j] - adj_water(i,j))
            if new_grid[i][j] > 0:
                new_search_list.append([i,j])
    visited = [[0]*M for _ in range(N)]
    cnt = 0
    for i,j in new_search_list:
        if not visited[i][j] and new_grid[i][j] > 0 :
            visited[i][j] = 1
            v = [[i,j]]
            cnt += 1
            while v:
                x,y = v.pop()
                for k in range(4):
                    nx,ny = x+dx[k],y+dy[k]
                    if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and new_grid[nx][ny] > 0:
                        visited[nx][ny] = 1
                        v.append([nx,ny])
    if cnt == 0:
        print(0)
        break
    elif cnt == 1:
        grid = new_grid
        search_list = new_search_list
        continue
    elif cnt > 1:
        print(year)
        break
