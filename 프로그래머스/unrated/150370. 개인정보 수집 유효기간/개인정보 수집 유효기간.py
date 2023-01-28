def calculate_date(today,exp):
    y,m,d = map(int,today.split("."))
    y2,exp = divmod(exp,12)
    if (d == 1):
        if(m+exp<11):
            return ".".join(map(str,[y+y2,"0"+str(m+exp-1),28]))
        elif(11<=m+exp<=13):
            return ".".join(map(str,[y+y2,m+exp-1,28]))
        else:
            if(m+exp-13 <= 9):
                m = "0"+str(m+exp-13)
            else:
                m = m + exp - 13
            return ".".join(map(str,[y+y2+1,m,28]))
    else:
        if(d <= 10):
            d = "0"+str(d-1)
        else:
            d = d - 1
        if(m+exp<10):
            return ".".join(map(str,[y+y2,"0"+str(m+exp),d]))
        elif(10<=m+exp<=12):
            return ".".join(map(str,[y+y2,m+exp,d]))
        else:
            if(m+exp-12 <= 9):
                m = "0"+str(m+exp-12)
            else:
                m = m + exp - 12
            return ".".join(map(str,[y+y2+1,m,d]))
            
def solution(today, terms, privacies):
    answer = []
    exp_dict = {}
    for term in terms:
        name,exp_duration = term.split()
        exp_dict[name] = int(exp_duration)
    for i in range(len(privacies)):
        date, name = privacies[i].split()
        exp_date = calculate_date(date,exp_dict[name])
        if(exp_date < today):
            answer.append(i+1)
    return answer