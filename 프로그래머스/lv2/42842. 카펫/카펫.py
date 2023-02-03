def solution(brown, yellow):
    sum_ = (brown - 4) // 2
    mul_ = yellow
    for i in range(1,sum_):
        a,b = sum_-i,i
        if a*b == mul_:
            return [a+2,b+2]