from itertools import combinations
while True:
  s = list(map(int,input().split()))
  if s[0] == 0:
    break
  k = s[0]
  s = s[1:]
  for c in combinations(s,6):
    print(*c)
  print()