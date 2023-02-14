def solution(array, commands):
    answer = []
    for com in commands:
        temp = array[com[0]-1:com[1]]
        temp.sort()
        answer.append(temp[com[2]-1])
    return answer