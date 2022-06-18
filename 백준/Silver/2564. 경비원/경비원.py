bw,bh = map(int,input().split())
n = int(input())
store_list = []
for _ in range(n):
    a,b = map(int,input().split())
    store_list.append([a,b])
x,y = map(int,input().split())
ans = 0
for store in store_list:
    a,b = store
    if a == x:
        ans += abs(y-b)
    elif (a==1 and x == 2) or (a==2 and x==1):
        ans += min(y+bh+b,(bw-y)+bh+(bw-b))
    elif (a==3 and x == 4) or (a==4 and x==3):
        ans += min(y+bw+b,(bh-y)+bw+(bh-b))
    elif a==1 and x==4:
        ans += bw-b + y
    elif a==4 and x==2:
        ans += bw-y + bh-b
    elif a==2 and x==3:
        ans += b + bh-y
    elif a==3 and x==1:
        ans += b + y
    elif x==1 and a==4:
        ans += bw-y + b
    elif x==4 and a==2:
        ans += bw-b + bh-y
    elif x==2 and a==3:
        ans += y + bh-b
    elif x==3 and a==1:
        ans += y + b
print(ans)