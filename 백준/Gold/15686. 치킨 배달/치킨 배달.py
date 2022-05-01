from itertools import combinations
n,m = map(int,input().split())
house = []
chicken = []
for i in range(n):
  row = list(map(int,input().split()))
  for j in range(n):
    if row[j] == 1:
      house.append([i,j])
    elif row[j] == 2:
      chicken.append([i,j])
answer = 10**9
for combi in combinations(chicken,m):
  dist = 0
  for h in house:
    c_dist = 100
    for c in combi:
      c_dist = min(c_dist,abs(h[0]-c[0])+abs(h[1]-c[1]))
    dist += c_dist
  answer = min(answer,dist)
print(answer)