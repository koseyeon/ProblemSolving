import sys
input = sys.stdin.readline
n = int(input())
weights = []
for _ in range(n):
    weights.append(int(input()))
weights.sort()
answer = 0
for i in range(len(weights)):
    answer = max(answer,weights[i]*(n-i))
print(answer)