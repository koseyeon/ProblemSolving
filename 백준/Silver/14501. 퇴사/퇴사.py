n = int(input())
dp = [0]*(n+1)
work = []
for i in range(n):
    work.append(list(map(int,input().split())))
for i in range(n):
    for j in range(i+work[i][0],n+1):
        dp[j] = max(dp[j],dp[i]+work[i][1])
print(dp[n])