from collections import deque
n,m = map(int,input().split())
graph = {}
for _ in range(m):
  a,b = map(int,input().split())
  if a not in graph.keys():
    graph[a] = [b]
  else:
    graph[a].append(b)
  if b not in graph.keys():
    graph[b] = [a]
  else:
    graph[b].append(a)
def kebin_bacon(x):
  sum_val = 0
  for y in range(1,n+1):
    if(y==x):
      continue
    visited = [0]*(n+1)
    visited[x] = 1
    rel = deque([])
    count = 1
    for c in graph[x]:
      visited[c]=1
      rel.append([c,count])
    while rel:
      [next,cnt] = rel.popleft()
      if(next == y):
        count = cnt
        break
      for nxt in graph[next]:
        if not visited[nxt]:
          visited[nxt]=1
          rel.append([nxt,cnt+1])
    sum_val += count
  return sum_val
count = 10**9
person_num = 1
for i in range(1,n+1):
  result = kebin_bacon(i)
  if(count>result):
    count = result
    person_num = i
print(person_num)
