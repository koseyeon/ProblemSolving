N,M,R = map(int,input().split())
board = []
for _ in range(N):
    board.append(list(map(int,input().split())))
oper_list = list(map(int,input().split()))
def op1():
    r,c = len(board),len(board[0])
    for i in range(r//2):
        board[i],board[r-1-i] = board[r-1-i],board[i]  
def op2():
    r,c = len(board),len(board[0])
    for i in range(r):
        for j in range(c//2):
            board[i][j],board[i][c-1-j] = board[i][c-1-j],board[i][j]
def op3():
    global board
    r,c = len(board),len(board[0])
    new_board = [[0]*r for _ in range(c)]
    for i in range(c):
        for j in range(r):
            new_board[i][j]=board[r-1-j][i]
    board = new_board
def op4():
    global board
    r,c = len(board),len(board[0])
    new_board = [[0]*r for _ in range(c)]
    for i in range(c):
        for j in range(r):
            new_board[i][j]=board[j][c-1-i]
    board = new_board
def op5():
    global board
    r,c = len(board),len(board[0])
    part1 = [board[i][:c//2] for i in range(r//2)]
    part2 = [board[i][c//2:] for i in range(r//2)]
    part3 = [board[i][c//2:] for i in range(r//2,r)]
    part4 = [board[i][:c//2] for i in range(r//2,r)]
    new_board = []
    for i in range(r//2):
        new_board.append(part4[i]+part1[i])
    for i in range(r//2):
        new_board.append(part3[i]+part2[i])
    board = new_board 
def op6():
    global board
    r,c = len(board),len(board[0])
    part1 = [board[i][:c//2] for i in range(r//2)]
    part2 = [board[i][c//2:] for i in range(r//2)]
    part3 = [board[i][c//2:] for i in range(r//2,r)]
    part4 = [board[i][:c//2] for i in range(r//2,r)]
    new_board = []
    for i in range(r//2):
        new_board.append(part2[i]+part3[i])
    for i in range(r//2):
        new_board.append(part1[i]+part4[i])
    board = new_board
for oper in oper_list:
    if oper == 1:
        op1()
    elif oper == 2:
        op2()
    elif oper == 3:
        op3()
    elif oper == 4:
        op4()
    elif oper == 5:
        op5()
    elif oper == 6:
        op6()
for i in range(len(board)):
    print(*board[i])