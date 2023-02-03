def solution(s):
    nums = list(map(int,s.split()))
    answer = " ".join([str(min(nums)),str(max(nums))])
    return answer