def solution(n,a,b):
    answer = 0
    cnt = 0
    if a>b:
        a,b = b,a
    while True:
        cnt += 1
        if b-a == 1 and b%2==0:
            break
        if a%2 == 0 and a//2 != 0:
            a = a//2
        else:
            a = a//2 + 1
        if b%2 == 0 and b//2 != 0:
            b = b//2 
        else:
            b = b//2 + 1
    return cnt