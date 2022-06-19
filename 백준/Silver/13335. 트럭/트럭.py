from collections import deque
n,w,L = map(int,input().split())
weights = deque(list(map(int,input().split())))
time = 0
now = deque([])
while weights or sum(now)!=0:
    if len(now)>=w:
        now.popleft()
    if weights:
        next = weights[0]
        if sum(now)+next <=L:
            now.append(next)
            weights.popleft()
        else:
            now.append(0)
    else:
        now.append(0)
    time+=1
print(time)