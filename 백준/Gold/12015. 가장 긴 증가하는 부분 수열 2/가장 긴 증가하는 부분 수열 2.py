n = int(input())
def bisect_left(lis,x):
  start = 0
  end = len(lis)-1
  mid = 0
  while start<=end:
    mid = (start+end)//2
    if lis[mid]==x:
      return mid
    elif lis[mid]<x:
      start = mid + 1
    else:
      end = mid - 1
  return start
nums = list(map(int,input().split()))
lis = [nums[0]]
for i in range(1,n):
  if lis[-1]<nums[i]:
    lis.append(nums[i])
  else:
    lis[bisect_left(lis,nums[i])]=nums[i]
print(len(lis))