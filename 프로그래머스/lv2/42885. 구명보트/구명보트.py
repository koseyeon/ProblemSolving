from collections import deque
def solution(people, limit):
    people.sort()
    d = deque(people)
    cnt = 0
    while len(d)>=2:
        if d[0]+d[-1] <= limit:
            d.pop()
            d.popleft()
            cnt += 2
        else:
            d.pop()
    return len(people)-cnt + cnt//2