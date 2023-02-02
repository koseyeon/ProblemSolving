def solution(price, money, count):
    answer = 0
    for i in range(count):
        money -= price*(i+1)
    if money >= 0:
        return 0
    else:
        return -money