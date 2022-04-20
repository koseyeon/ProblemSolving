t = int(input()) 
dp = [ [[0]*22 for _ in range(22)] for _ in range(22) ]
dp[1][1][1]=1
dp[2][1][2]=1
dp[2][2][1]=1
dp[3][1][2]=1
dp[3][2][1]=1
dp[3][2][2]=2
dp[3][1][3]=1
dp[3][3][1]=1
for i in range(4,21):
  for j in range(1,21):
    for k in range(1,21):
      if dp[i-1][j][k]!=0:
        dp[i][j][k]+=dp[i-1][j][k]*(i-2)
        dp[i][j+1][k] += dp[i-1][j][k]
        dp[i][j][k+1] += dp[i-1][j][k]
for _ in range(t):
  n,l,r = map(int,input().split())
  print(dp[n][l][r])