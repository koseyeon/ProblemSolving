def solution(food):
    temp = ""
    for i in range(1,len(food)):
        temp += str(i)*(food[i]//2)
    temp2 = temp
    temp += "0"
    for i in range(len(temp2)-1,-1,-1):
        temp += temp2[i]
    return temp