def isInOrbit(x,y,cx,cy,r):
    return (x-cx)**2 + (y-cy)**2 < r**2
t = int(input())
for _ in range(t):
    cnt = 0
    x1,y1,x2,y2 = map(int,input().split())
    n = int(input())
    for _ in range(n):
        cx,cy,r = map(int,input().split())
        if isInOrbit(x1,y1,cx,cy,r) and isInOrbit(x2,y2,cx,cy,r):
            continue
        if isInOrbit(x1,y1,cx,cy,r):
            cnt += 1
        if isInOrbit(x2,y2,cx,cy,r):
            cnt += 1
    print(cnt)