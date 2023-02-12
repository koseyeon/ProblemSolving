from collections import defaultdict
def solution(participant, completion):
    d = defaultdict(int)
    for i in range(len(participant)):
        d[participant[i]] += 1
    for i in range(len(completion)):
        d[completion[i]] -= 1
    for i in range(len(participant)):
        if d[participant[i]] == 1:
            return participant[i]
    