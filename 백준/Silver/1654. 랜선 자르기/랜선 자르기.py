k,n = map(int,input().split())
lines = []
for _ in range(k):
  lines.append(int(input()))
lines.sort()
lo,hi = 1,lines[-1]
def Check(x):
  cut_num = 0
  for line in lines:
    cut_num += line//x
  if(cut_num>=n):
    return True
  else:
    return False
while lo<=hi:
  mid = (lo+hi)//2
  if(Check(mid)):
    lo = mid+1
  else:
    hi = mid-1
print(hi)