from collections import defaultdict
def solution(X, Y):
    d1 = defaultdict(int)
    d2 = defaultdict(int)
    d = {}
    for i in range(len(X)):
        d1[X[i]] += 1
    for i in range(len(Y)):
        d2[Y[i]] += 1
    for i in range(10):
        num = min(d1[str(i)],d2[str(i)])
        if num == 0:
            continue
        d[str(i)] = num
    if len(d.keys()) == 0:
        return "-1"
    if len(d.keys()) == 1 and "0" in d.keys():
        return "0"
    nums = list(d.items())
    nums.sort(reverse=True)
    answer = ""
    for num in nums:
        answer += num[0]*num[1]
    return answer
    