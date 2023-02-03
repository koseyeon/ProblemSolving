def solution(prices):
    answer = [0]*len(prices)
    s = []
    for i in range(len(prices)):
        while s:
            if s[-1][0] > prices[i]:
                v,idx = s.pop()
                answer[idx] = i - idx
            else:
                break
        s.append([prices[i],i])
    for i in range(len(s)):
        v,idx = s.pop()
        answer[idx] = len(prices)-1 - idx
    return answer