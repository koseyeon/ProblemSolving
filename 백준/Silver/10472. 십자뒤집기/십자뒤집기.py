from collections import deque


p = int(input())
def click(x,y,old_board):
    new_board = [r[:] for r in old_board]
    case = [[x,y],[x+1,y],[x-1,y],[x,y+1],[x,y-1]]
    for c in case:
        q,w = c
        if 0<=q<3 and 0<=w<3:
            if new_board[q][w] == '*':
                new_board[q][w]='.'
            else:
                new_board[q][w]='*'
    return new_board
def trans_to_binany(board):
    bin = ''
    for i in range(3):
        for j in range(3):
            if board[i][j]=='.':
                bin+='0'
            else:
                bin+='1'
    return int(bin,2)
for _ in range(p):
    target = []
    for _ in range(3):
        target.append(list(input()))
    visited = [0]*(2**9)
    init_board = [['.','.','.'] for _ in range(3)]
    visited[0]=1
    d = deque([[init_board,0]])
    while d:
        board,cnt = d.popleft()
        if board == target:
            print(cnt)
            break
        for i in range(3):
            for j in range(3):
                new_board = click(i,j,board)
                bin = trans_to_binany(new_board)
                if visited[bin] == 0:
                    visited[bin] = 1
                    d.append([new_board,cnt+1])