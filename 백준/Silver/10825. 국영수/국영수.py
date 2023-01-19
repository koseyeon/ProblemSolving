import sys
import functools
input = sys.stdin.readline
n = int(input())
score = []
for _ in range(n):
  score.append(list(input().split()))
def cmp_func(a,b):
  if int(a[1]) > int(b[1]):
    return -1
  elif int(a[1]) < int(b[1]):
    return 1
  if int(a[2]) < int(b[2]):
    return -1
  elif int(a[2]) > int(b[2]):
    return 1
  if int(a[3]) > int(b[3]):
    return -1
  elif int(a[3]) < int(b[3]):
    return 1
  if a[0] < b[0]:
    return -1
  elif a[0] > b[0]:
    return 1
  else:
    return 0
score.sort(key=functools.cmp_to_key(cmp_func))
for s in score:
  print(s[0])

  


