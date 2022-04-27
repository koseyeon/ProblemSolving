n = int(input())
def H(n,r):
  ans = n+r-1
  cnt = 1
  while cnt<r:
    ans *=(n+r-1-cnt) 
    cnt +=1
  while r>1:
    ans//=r
    r-=1
  return ans
print(H(10,n)%10007)