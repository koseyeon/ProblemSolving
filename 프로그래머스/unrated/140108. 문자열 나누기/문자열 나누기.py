def solution(s):
    answer = 0
    i = 0
    x = s[i]
    a = 0
    b = 0
    while i <= len(s) - 1:
        if(i == len(s) - 1):
            answer += 1
            break
        if(s[i] == x):
            a += 1
        else:
            b += 1
        if a == b:
            answer += 1
            a = 0
            b = 0
            i += 1
            x = s[i]
            continue
        i += 1
        
    return answer