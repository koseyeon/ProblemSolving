n,m = map(int,input().split())
nums = [0]+list(map(int,input().split()))
psum = [0]*(n+1)
rem = [0]*(m+1)
for i in range(1,n+1):
  psum[i]=psum[i-1]+nums[i]
for i in range(1,n+1):
  psum[i]%=m
  rem[psum[i]]+=1
ans = 0
def combi_2(n):
  if n<2:
    return 0
  return n*(n-1)//2
for i in range(0,m):
  ans += combi_2(rem[i])
ans+=rem[0]
print(ans)