import sys
input = sys.stdin.readline
n = int(input())
tops = list(map(int,input().split()))
stack = [[0,0]]
answer = []
for i in range(n):
  now = tops[i]
  while len(stack)>0:
    if stack[-1][0]<now:
      stack.pop()
    else:
      answer.append(str(stack[-1][1]))
      stack.append([tops[i],i+1])
      break
  if len(stack)==0:
    answer.append(str(0))
    stack.append([tops[i],i+1])
print(" ".join(answer))