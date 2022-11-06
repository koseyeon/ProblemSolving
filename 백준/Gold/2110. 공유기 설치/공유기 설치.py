import sys
input = sys.stdin.readline
n,c = map(int,input().split())
houses = []
for _ in range(n):
  houses.append(int(input()))
houses.sort()
start,end = 0, houses[n-1]-houses[0]
result = 0
while start<=end:
  mid = (start+end)//2
  last = houses[0]
  count = 1
  for i in range(n):
    if houses[i]-last >= mid:
      count+=1
      last = houses[i]
  if count>=c:
    start = mid+1
    result = mid
  else:
    end = mid-1
print(result)