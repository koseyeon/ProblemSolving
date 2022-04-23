R,C = map(int,input().split())

arr = [list(input()) for _ in range(R)]
check = [['']*C for _ in range(R)]

stack = [(0,0,1,arr[0][0])]
result = 0
dx = [-1,1,0,0]
dy = [0,0,1,-1]
while stack:
    x,y,cnt,total = stack.pop()
    if result < cnt:
        result = cnt
    if result == 26:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0<= ny <C:
            if arr[nx][ny] not in total:
                temp = total + arr[nx][ny]
                if check[nx][ny] != temp:
                    check[nx][ny] = temp
                    stack.append((nx,ny,cnt+1,temp))
print(result)