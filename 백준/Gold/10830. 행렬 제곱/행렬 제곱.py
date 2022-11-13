import sys
import copy
input = sys.stdin.readline
n,b = map(int,input().split())
matrix = []
for _ in range(n):
  matrix.append(list(map(int,input().split())))
def multi(target1,target2):
  result = [[0]*n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      for k in range(n):
        result[i][j] += target1[i][k] * target2[k][j]
      result[i][j] %= 1000
  return result
def mod1000(target):
  result = [[0]*n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      result[i][j] = matrix[i][j]%1000
  return result
factor = []
x = 1
while b>0:
  if b >= x:
    x*=2
  else:
    factor.append(x//2)
    b-=x//2
    x=1 
dict = {}
dict[1] = mod1000(matrix)
f = factor[0]
x = 1
while x<f:
  x*=2
  dict[x] = multi(dict[x//2],dict[x//2])
result = dict[f]
for i in range(1,len(factor)):
  result = multi(result,dict[factor[i]])
for i in range(n):
  print(" ".join(map(str,result[i])))