answer = []
used = []
def solution(tickets):
    global answer,used
    for i,ticket in enumerate(tickets):
        a,b = ticket
        if a == "ICN":
            used = [0]*len(tickets)
            used[i] = 1
            path = [a,b]
            def backtracking(now,path):
                global answer,used
                if 0 not in used:
                    answer.append("-".join(path))
                    return
                for j,ticket in enumerate(tickets):
                    a,b = ticket
                    if used[j] == 0 and now == a:
                        used[j] = 1
                        backtracking(b,path+[b])
                        used[j] = 0
            backtracking(b,path)
    return sorted(answer)[0].split("-")