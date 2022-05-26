import sys
input = sys.stdin.readline
n,m,b = map(int,input().split())
ground = []
for _ in range(n):
    l = list(map(int,input().split()))
    for a in l:
        ground.append(a)
maxh, minh = max(ground),min(ground)
time_list = []
for h in range(minh,maxh+1):
    up_count,down_count,time = 0,0,0
    for g in ground:
        if g<h:
            down_count += h-g
        elif g>h:
            up_count += g-h
    if up_count+b>=down_count:
        time += up_count * 2
        time += down_count
        time_list.append([time,h])
time_list.sort(key=lambda x:(x[0],-x[1]))
print(time_list[0][0],time_list[0][1])