import heapq
def solution(operations):
    q1 = []
    q2 = []
    for o in operations:
        inst, num = o.split()
        if inst == "I":
            heapq.heappush(q1,int(num))
            heapq.heappush(q2,-int(num))
        elif num == "1" and q2:
            x = heapq.heappop(q2)
            q1.remove(-x)
        elif num == "-1" and q1:
            x = heapq.heappop(q1)
            q2.remove(-x)
    if not q1:
        return [0,0]
    else:
        return [-heapq.heappop(q2),heapq.heappop(q1)]
        