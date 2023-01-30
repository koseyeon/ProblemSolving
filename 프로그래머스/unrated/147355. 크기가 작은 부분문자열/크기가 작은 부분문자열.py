def solution(t, p):
    lt = len(t)
    lp = len(p)
    answer = 0
    for i in range(0,lt-lp+1):
        target = t[i:i+lp]
        if(target <= p):
            answer += 1
    return answer