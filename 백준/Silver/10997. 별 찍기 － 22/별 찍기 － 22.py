board = []
def remove(x,y,k):
    pass
n = int(input())
if n == 1:
    print("*")
else:
    board = [["*"]*(4*(n-1)+1) for _ in range(4*(n-1)+3)]
    x,y = 1,1
    k = 1
    while k<n:
        for i in range(y,y+4*(n-k)):
            board[x][i] = ' '
        for i in range(x,x+4*(n-k)+1):
            board[i][y] = ' '
        for i in range(y,y+4*(n-k)-1):
            board[x+4*(n-k)][i] = ' '
        for i in range(x+4*(n-k),x+1,-1):
            board[i][y+4*(n-k)-2] = ' '
        k+=1
        x+=2
        y+=2
    for i in range(len(board)):
        if i == 1:
            print("*")
        else:
            print(''.join(board[i]))
    
