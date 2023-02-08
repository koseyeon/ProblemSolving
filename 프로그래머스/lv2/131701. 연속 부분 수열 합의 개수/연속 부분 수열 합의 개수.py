def solution(elements):
    l = len(elements)
    s = set()
    for i in range(l):
        a = elements[i]
        s.add(a)
        for j in range(i+1,i+l):
            a += elements[j%l]
            s.add(a)
    return len(s)