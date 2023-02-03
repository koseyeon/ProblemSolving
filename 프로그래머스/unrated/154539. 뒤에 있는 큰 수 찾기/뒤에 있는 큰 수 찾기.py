def solution(numbers):
    answer = [0]*len(numbers)
    s = []
    for i in range(len(numbers)):
        while s:
            if numbers[i] > s[-1][0]:
                v,idx = s.pop()
                answer[idx] = numbers[i]
            else:
                break
        s.append([numbers[i],i])
    while s:
        v,idx = s.pop()
        answer[idx] = -1
    return answer