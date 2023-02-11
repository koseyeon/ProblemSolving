def solution(d, budget):
    answer = 0
    d.sort(reverse=True)
    while d:
        a = d.pop()
        if a > budget:
            break
        budget-=a
        answer+=1
    return answer