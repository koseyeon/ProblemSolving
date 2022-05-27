from itertools import permutations
n = int(input())
nums = list(map(int,input().split()))
plus,minus,multi,divide = map(int,input().split())
def operate(a,b,oper):
    if oper == '+':
        return a+b
    elif oper == '-':
        return a-b
    elif oper == '*':
        return a*b
    else:
        if a<0 and b>0:
            return -(abs(a)//b)
        else:
            return a//b
combi_list = []
def combi(plus,minus,multi,divide,c,k):
    if k == 0:
        combi_list.append(c)
        return
    if plus>0:
        combi(plus-1,minus,multi,divide,c+['+'],k-1)
    if minus>0:
        combi(plus,minus-1,multi,divide,c+['-'],k-1)
    if multi>0:
        combi(plus,minus,multi-1,divide,c+['*'],k-1)
    if divide>0:
        combi(plus,minus,multi,divide-1,c+['/'],k-1)
combi(plus, minus, multi, divide, [], n-1)
min_v = 10**9
max_v = -10**9
for c in combi_list:
    ans = nums[0]
    i = 1
    while c:
        oper = c.pop()
        ans = operate(ans,nums[i],oper)
        i+=1
    min_v = min(ans,min_v)
    max_v = max(ans,max_v)
print(max_v)
print(min_v)