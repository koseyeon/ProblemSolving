from collections import deque
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
degree = [0]*(n+1)
for _ in range(m):
  a,b = map(int,input().split())
  graph[a].append(b)
  degree[b]+=1
d = deque([])
for i in range(1,n+1):
  if degree[i]==0:
    d.append(i)
ans = ''
while d:
  x = d.popleft()
  for next in graph[x]:
    degree[next]-=1
    if degree[next]==0:
      d.append(next)
  print(x,end=" ")