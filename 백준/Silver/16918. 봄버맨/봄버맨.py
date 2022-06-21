r,c,n = map(int,input().split())
board = []
for _ in range(r):
    board.append(list(input()))
dx = [1,0,-1,0]
dy = [0,1,0,-1]
def boom(x,y,cnt):
    board[x][y]='.'
    for i in range(2):
        nx,ny = x+dx[i],y+dy[i]
        if 0<=nx<r and 0<=ny<c and board[nx][ny]!=str(cnt) and board[nx][ny]!='O':
            board[nx][ny]='.'
    for i in range(2,4):
        nx,ny = x+dx[i],y+dy[i]
        if 0<=nx<r and 0<=ny<c:
            board[nx][ny]='.'
for i in range(2,n+1):
    if i%2==0:
        for j in range(r):
            for k in range(c):
                if board[j][k] == '.':
                    board[j][k] = str(i)
    else:
        for j in range(r):
            for k in range(c):
                if board[j][k] == str(i-3) or board[j][k] == 'O':
                    boom(j,k,i-3)
for i in range(r):
    for j in range(c):
        if board[i][j] != '.':
            board[i][j] = 'O'
for i in range(r):
    for j in range(c):
        print(board[i][j],end="")
    print()