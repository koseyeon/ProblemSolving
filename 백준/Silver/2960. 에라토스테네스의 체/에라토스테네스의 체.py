n,k = map(int,input().split())
nums = [0]*(n+1)
cnt = 0
now = 2
while cnt < k:
    for i in range(now,n+1):
        if nums[i]==0:
            now = i
            break
    for i in range(now,n+1):
        if i%now==0 and nums[i]==0:
            nums[i]=1
            cnt+=1
            if cnt == k:
                print(i)
                break

