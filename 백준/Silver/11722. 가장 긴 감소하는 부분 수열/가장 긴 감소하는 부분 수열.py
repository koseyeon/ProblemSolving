
n = int(input())
nums = list(map(int,input().split()))
dp = []
for num in nums:
  dp.append([num,1])
for i in range(n):
  for j in range(i):
    if dp[i][0] < dp[j][0] and dp[i][1] < dp[j][1] + 1:
      dp[i] = [dp[i][0],dp[j][1]+1]
ans = 0
for i in range(n):
  if dp[i][1] > ans:
    ans = dp[i][1]
print(ans)
