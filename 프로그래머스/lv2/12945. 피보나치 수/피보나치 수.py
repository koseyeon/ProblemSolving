def solution(n):
    answer = 0
    temp = [0,1]
    for i in range(2,n+1):
        temp.append((temp[-2]+temp[-1])%1234567)
    return temp[n]