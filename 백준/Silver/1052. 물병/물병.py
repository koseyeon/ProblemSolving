n,k = map(int,input().split())
cnt = 0
extra = n
def biggest(x):
    a = 1
    while a<=x:
        a*=2
    return a//2
def check(x):
    while x>1:
        if x%2!=0:
            return False
        else:
            x=x//2
    return True    
if n <= k:
    print(0) 
elif check(n):
    print(0)
elif k == 1:
    print(biggest(extra)*2-extra)
else:
    while True:
        biggest_part = biggest(extra)
        extra -= biggest_part
        cnt +=1
        if extra == biggest_part:
            cnt-=1
        if cnt+1>=k:
            if check(extra):
                print(max(0,cnt+1-k))
            else:
                print(biggest(extra)*2-extra)
            break
        elif check(extra):
            print(max(0,cnt+1-k))
            break