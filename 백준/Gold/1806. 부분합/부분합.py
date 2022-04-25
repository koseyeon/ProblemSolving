n,s = map(int,input().split())
num = [0]+list(map(int,input().split()))
psum =[0]*(n+1)
for i in range(1,n+1):
  psum[i]=psum[i-1]+num[i]
p1,p2 = 1,0
ans = 10**9
while p1<=n and p2<=n:
  if psum[p1]-psum[p2] < s:
    p1+=1
  elif psum[p1]-psum[p2] >= s:
    ans = min(ans,p1-p2)
    p2+=1
if ans == 10**9:
  print(0)
else:
  print(ans)
