def solution(s):
    d = {}
    answer = []
    for i in range(len(s)):
        if s[i] not in d.keys():
            d[s[i]] = i
            answer.append(-1)
        else:
            answer.append(i-d[s[i]])
            d[s[i]] = i
    return answer