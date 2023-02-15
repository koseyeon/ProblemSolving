def solution(number, k):
    s = []
    for n in number:
        while s and s[-1] < n and k > 0:
            s.pop()
            k -= 1
        s.append(n)
    while k>0:
        s.pop()
        k -= 1    
    return "".join(s)