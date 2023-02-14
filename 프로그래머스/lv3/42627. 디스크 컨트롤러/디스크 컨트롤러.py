import heapq

def solution(jobs):
    jobs_cnt = len(jobs)
    total = 0
    end = 0
    jobs.sort(key=lambda x: (x[0]+x[1],x[0]))
    jobs = [[(x[0],x[0]+x[1]),x[0]+x[1],x[0]] for x in jobs]
    heapq.heapify(jobs)
    while jobs:
        order, next_end, next_start = heapq.heappop(jobs)
        if next_start >= end :
            end = next_end
            total += next_end - next_start
        else:
            waiting = end - next_start 
            total += waiting
            new_order = (end,next_end+waiting)
            heapq.heappush(jobs,[new_order,next_end + waiting,end])
    return total//jobs_cnt