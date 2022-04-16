n = int(input())
cards = list(map(int,input().split()))
dp = [0]+cards[:]
for i in range(1,n+1):
  for j in range(1,i):
    dp[i] = max(dp[i],dp[j]+dp[i-j])
print(max(dp))