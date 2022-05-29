from collections import deque

board = []
for _ in range(19):
    board.append(list(map(int,input().split())))
def get_nextPos(x,y,direction):
    if direction == 0:
        return x,y+1,x,y-1
    elif direction == 1:
        return x+1,y,x-1,y
    elif direction == 2:
        return x-1,y+1,x+1,y-1
    elif direction == 3:
        return x+1,y+1,x-1,y-1
def bfs(x,y,type,direction):
    visited = [[0] * 19 for _ in range(19)]
    visited[x][y]=1
    d = deque([[x,y]])
    count = 1
    history = [[x,y]]
    while d:
        x,y = d.popleft()
        nx1,ny1,nx2,ny2 = get_nextPos(x,y,direction)
        if 0<=nx1<19 and 0<=ny1<19 and board[nx1][ny1]==type and visited[nx1][ny1]==0:
            visited[nx1][ny1]=1
            d.append([nx1,ny1])
            history.append([nx1,ny1])
            count+=1
        if 0<=nx2<19 and 0<=ny2<19 and board[nx2][ny2]==type and visited[nx2][ny2]==0:
            visited[nx2][ny2]=1
            d.append([nx2,ny2])
            history.append([nx2,ny2])
            count+=1
    return count,history
found = False
for i in range(19):
    for j in range(19):
        for k in range(4):
            if board[i][j]!=0:
                count,history = bfs(i,j,board[i][j],k)
                if count == 5:
                    history.sort(key=lambda x:(x[1],x[0]))
                    print(board[i][j])
                    print(history[0][0]+1,history[0][1]+1)
                    found = True
                    break
        if found:
            break
    if found:
        break
if not found:
    print(0)

