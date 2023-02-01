import sys
input = sys.stdin.readline
n,m = map(int,input().split())
nums = []
for _ in range(n):
    nums.append(list(map(int,input().split())))
acc = [[0]*m for _ in range(n)]
for i in range(m):
    acc[0][i] = nums[0][i]
for i in range(m):
    for j in range(n):
        acc[j][i] = acc[j-1][i] + nums[j][i]
k = int(input())
for _ in range(k):
    i,j,x,y = map(int,input().split())
    answer = 0
    for a in range(j-1,y):
        if i-2 == -1:
            answer += acc[x-1][a]
        else:
            answer += acc[x-1][a] - acc[i-2][a]
    print(answer)
