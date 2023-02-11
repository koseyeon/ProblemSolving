from itertools import combinations

def isPrime(k):
    for i in range(2,int(k**0.5)+1):
        if k%i == 0:
            return False
    return True
def solution(nums):
    answer = 0
    for c in combinations(nums,3):
        s = sum(c)
        if isPrime(s):
            answer += 1
    return answer