def solution(maps):
    answer = []
    w = len(maps[0])
    h = len(maps)
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    visited = [[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if maps[i][j].isdigit() and not visited[i][j]:
                visited[i][j] = 1
                s = [[i,j]]
                cnt = int(maps[i][j])
                while s:
                    x,y = s.pop()
                    for k in range(4):
                        nx,ny = x+dx[k],y+dy[k]
                        if 0<=nx<h and 0<=ny<w and not visited[nx][ny] and maps[nx][ny].isdigit():
                            visited[nx][ny] = 1
                            cnt += int(maps[nx][ny])
                            s.append([nx,ny])
                answer.append(cnt)
    if len(answer) == 0:
        return [-1]
    answer.sort()
    return answer