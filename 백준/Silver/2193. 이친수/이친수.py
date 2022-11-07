# N자리 이친수(10...) 개수는 N-2자리 이친수 + N-3자리이친수 개수 + N-4자리이친수 + ... + 1자리 이친수 개수 + 1와 같다.
n = int(input())
dp = [0]*(91)
dp[1]=1
dp[2]=1
dp[3]=2
if(n<=3):
  print(dp[n])
else:
  for i in range(4,n+1):
    for j in range(1,i-1):
      dp[i]+=dp[j]
    dp[i]+=1
  print(dp[n])

