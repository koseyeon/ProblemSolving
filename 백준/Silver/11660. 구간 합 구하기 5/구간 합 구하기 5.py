import sys
input = sys.stdin.readline
n,m = map(int,input().split())
grid = []
for _ in range(n):
  grid.append(list(map(int,input().split())))
acc_table = [[0]*n for _ in range(n)]
acc_table2 = [[0]*n for _ in range(n)]
for i in range(n):
  for j in range(n):
    temp = grid[i][j]
    if j!=0:
      temp += acc_table[i][j-1]
    if i!=0:
      temp += acc_table2[i-1][j]
      acc_table2[i][j] = acc_table2[i-1][j] + grid[i][j]
    else:
      acc_table2[i][j] = grid[i][j]
    acc_table[i][j] = temp
for _ in range(m):
  x1,y1,x2,y2 = map(int,input().split())
  part1,part2,part3 = 0,0,0
  ans = 0
  if y1 != 1:
    part1 = acc_table[x2-1][y1-2]
  if x1 != 1:
    part2 = acc_table[x1-2][y2-1]
  if x1 != 1 and y1 != 1:
    part3 = acc_table[x1-2][y1-2]
    ans = acc_table[x2-1][y2-1] - part1 - part2 + part3
  else:
    ans = acc_table[x2-1][y2-1] - part1 - part2
  print(ans)
  
