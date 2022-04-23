n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
degree = [0]*(n+1)
for _ in range(m):
  a,b = map(int,input().split())
  graph[b].append(a)
  degree[a]+=1
s = []
for i in range(1,n+1):
  if degree[i]==0:
    s.append(i)
ans = []
while s:
  x = s.pop()
  ans.append(str(x))
  for next in graph[x]:
    degree[next]-=1
    if degree[next]==0:
      s.append(next)
print(' '.join(reversed(ans)))