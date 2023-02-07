def solution(citations):
    for i in range(0,10001):
        cnt = 0
        for j in range(len(citations)):
            if citations[j] >= i:
                cnt += 1
        if cnt < i:
            return i - 1