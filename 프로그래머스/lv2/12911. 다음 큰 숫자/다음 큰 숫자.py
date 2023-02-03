def solution(n):
    b = format(n,"b")
    if "1"*len(b) == b or (b.count("0") == 1 and b[-1] == "0"):
        next = sorted(list(b+"0"))
        next = [next[-1]] + next[:-1]
        return int("".join(next),2)
    next = list(b)
    idx = 0
    for i in range(len(next)-1,-1,-1):
        if next[i] == "1" and next[i-1] == "0":
            next[i],next[i-1] = next[i-1],next[i]
            idx = i
            break
    next = next[:idx+1] + sorted(next[idx+1:])
    return int("".join(next),2)
    