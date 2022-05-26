from itertools import permutations
n = int(input())
rules = list(map(int,input().split()))

for pe in permutations([i for i in range(1,n+1)],n):
    bigger_left = {}
    for i in range(1,n+1):
        bigger_left[i]=0
    for i in range(n):
        for j in range(i):
            if pe[j]>pe[i]:
                bigger_left[pe[i]] += 1
    find = True
    for i in range(len(rules)):
        if rules[i] != bigger_left[i+1]:
            find=False
            break
    if find:
        print(*pe)