n = int(input())
count = int(input())
nums = list(map(int,input().split()))
board = [[101,0,0] for _ in range(n)]
time = 0
def find_from_board(num):
    found = False
    for i in range(n):
        if board[i][0]==num:
            board[i][1]+=1
            found = True
            return True
    if not found:
        return False
def change_board(num):
    temp = sorted(board,key=lambda x:(x[1],x[2]))
    prev_num = temp[0][0]
    for i in range(n):
        if board[i][0]==prev_num:
            board[i] = [num,1,time]
            return
for num in nums:
    time+=1
    result = find_from_board(num)
    if result == True:
        continue
    else:
        change_board(num)
board.sort()
result = []
for i in range(n):
    if board[i][0]!=101:
        result.append(board[i][0])
    else:
        break
print(*result)