def binary(num):
    result = []
    while num!=0:
        num,r = divmod(num,2)
        result.append(r)
    return "".join([str(result[i]) for i in range(len(result)-1,-1,-1)])
def solution(s):
    answer = []
    try_cnt = 0
    zero_cnt = 0
    while s != "1":
        zcnt = len(s) - s.count("1")
        zero_cnt += zcnt
        s = binary(len(s) - zcnt)
        try_cnt += 1
    return [try_cnt,zero_cnt]