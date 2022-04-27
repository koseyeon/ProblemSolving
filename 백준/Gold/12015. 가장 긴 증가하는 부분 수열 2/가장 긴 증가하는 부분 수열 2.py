import bisect
n = int(input())
nums = list(map(int,input().split()))
lis = [nums[0]]
for i in range(1,n):
  if lis[-1]<nums[i]:
    lis.append(nums[i])
  elif lis[-1]==nums[i]:
    continue
  else:
    if lis[bisect.bisect(lis,nums[i])-1]==nums[i]:
      continue
    else:
      lis[bisect.bisect(lis,nums[i])]=nums[i]
print(len(lis))
