from collections import defaultdict,deque
import sys
input = sys.stdin.readline
k = int(input())
def is_binary_graph(v,graph):
  visited = [-1]*(v+1)
  for i in range(1,v+1):
    if(visited[i] == -1):
      color = True
      visited[i] = color
    else:
      continue
    dq = deque([i])
    while dq:
      now = dq.popleft()
      color = visited[now]
      for nxt in graph[now]:
        if visited[nxt]==color:
          return False
        elif visited[nxt]==-1:
          visited[nxt] = not color
          dq.append(nxt)
  return True
for _ in range(k):
  v,e = map(int,input().split())
  graph = defaultdict(list)
  for _ in range(e):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
  result = is_binary_graph(v,graph)
  if(result==True):
    print("YES")
  else:
    print("NO")
  