def get_score(a,b,choice):
    if choice == 1:
        return [a,3]
    elif choice == 2:
        return [a,2]
    elif choice == 3:
        return [a,1]
    elif choice == 4:
        return [a,0]
    elif choice == 5:
        return [b,1]
    elif choice == 6:
        return [b,2]
    elif choice == 7:
        return [b,3]
def solution(survey, choices):
    answer = ''
    d = {}
    d["R"] = 0
    d["T"] = 0
    d["C"] = 0
    d["F"] = 0
    d["J"] = 0
    d["M"] = 0
    d["A"] = 0
    d["N"] = 0
    for i in range(len(survey)):
        kind,score = get_score(survey[i][0],survey[i][1],choices[i])
        d[kind] += score
    
    if d["R"] >= d["T"]:
        answer += "R"
    else:
        answer += "T"
        
    if d["C"] >= d["F"]:
        answer += "C"
    else:
        answer += "F"
    
    if d["J"] >= d["M"]:
        answer += "J"
    else:
        answer += "M"
        
    if d["A"] >= d["N"]:
        answer += "A"
    else:
        answer += "N"
    return answer