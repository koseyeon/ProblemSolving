n = int(input())
dp = [0]*(n+1)
work = []
for i in range(n):
    work.append(list(map(int,input().split())))
for i in range(n-1,-1,-1):
    if i+work[i][0]<=n:
        dp[i] = max(dp[i+1],dp[i+work[i][0]]+work[i][1])
    else:
        dp[i] = max(dp[i],dp[i+1])
print(dp[0])