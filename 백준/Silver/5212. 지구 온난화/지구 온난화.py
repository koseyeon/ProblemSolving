r,c = map(int,input().split())
board = [list(input()) for _ in range(r)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]
def check(x,y):
    cnt = 0
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if nx<0 or nx>r-1 or ny<0 or ny>c-1:
            cnt+=1
            continue
        if board[nx][ny]=='.':
            cnt+=1
    return True if cnt>=3 else False
next_board = [ row[:] for row in board ]
x1,y1,x2,y2 = 10,10,-1,-1
for i in range(r):
    for j in range(c):
        if board[i][j]=='X':
            if check(i,j) == True:
                next_board[i][j] = '.'
            else:
                x1 = min(x1,i)
                y1 = min(y1,j)
                x2 = max(x2,i)
                y2 = max(y2,j)
for i in range(x1,x2+1):
    for j in range(y1,y2+1):
        print(next_board[i][j],end="")
    print()
