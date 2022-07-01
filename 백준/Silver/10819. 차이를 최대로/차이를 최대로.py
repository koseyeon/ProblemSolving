from itertools import permutations
n = int(input())
nums = list(map(int,input().split()))
ans = 0
for p in permutations(nums,n):
    t = 0
    for i in range(n-1):
        t += abs(p[i]-p[i+1])
    ans = max(ans,t)
print(ans)