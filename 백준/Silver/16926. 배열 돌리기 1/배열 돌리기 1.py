n, m, r = map(int, input().split())
grid = []
def rotate(i, r):
    target = grid[i][i:m-i-1] + [grid[k][m-i-1] for k in range(i, n-i-1)] + \
             [grid[n-i-1][k] for k in range(m-i-1, i, -1)] + [grid[k][i] for k in range(n-i-1, i, -1)]
    target = target[r%len(target):] + target[:r%len(target)]
    target.reverse()
    for k in range(i, m-i-1):
        grid[i][k] = target.pop()
    for k in range(i,n-i-1):
        grid[k][m-i-1] = target.pop()
    for k in range(m-i-1,i,-1):
        grid[n-i-1][k] = target.pop()
    for k in range(n-i-1,i,-1):
        grid[k][i] = target.pop()
for j in range(n):
    grid.append(list(map(int, input().split())))
for i in range(min(n, m)//2):
    rotate(i, r)
for g in grid:
    print(*g)

