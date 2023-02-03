def lcm(a,b):
    gcd = 0
    result = 0
    for i in range(1,min(a,b)+1):
        if a%i == 0 and b%i == 0:
            gcd = max(result,i)
    return a//gcd * b//gcd * gcd
def solution(arr):
    arr2 = arr[:]
    result = arr2[-1]
    while arr2:
        result = lcm(result,arr2.pop())
    return result