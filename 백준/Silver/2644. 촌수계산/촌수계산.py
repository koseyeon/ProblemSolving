from collections import deque
n = int(input())
a,b = map(int,input().split())
m = int(input())
graph = {}
for _ in range(m):
  x,y = map(int,input().split())
  if(x not in graph.keys()):
    graph[x] = [y]
  else:
    graph[x].append(y)
  if(y not in graph.keys()):
    graph[y] = [x]
  else:
    graph[y].append(x)
visited = [0]*(n+1)
cnt = 1
rel = deque([])
visited[a] = 1
for c in graph[a]:
  visited[c] = 1
  rel.append([c,cnt])
found = False
while rel:
  [next,c] = rel.popleft()
  if next == b:
    found = True
    cnt = c
    break
  for nxt in graph[next]:
    if not visited[nxt]:    
      visited[nxt] = 1
      rel.append([nxt,c+1])
if found:
  print(cnt)
else:
  print(-1)