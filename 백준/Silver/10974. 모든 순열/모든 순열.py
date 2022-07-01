from itertools import permutations
n = int(input())
l = [i for i in range(1,n+1)]
for p in permutations(l,n):
    print(*p)