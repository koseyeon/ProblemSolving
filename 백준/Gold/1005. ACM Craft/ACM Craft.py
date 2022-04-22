from collections import deque
def topo_sort():
  s = []
  for i in range(1,n+1):
    if degree[i]==0 and target_check(i,target):
      s.append(i)
  d = deque([s])
  while d:
    waiting = d.popleft()
    next = []
    for w in waiting:
      if dp[w]:
        times[w]+=max(dp[w])
      if w == target:
        return
      for a in graph[w]:
        dp[a].append(times[w])
        degree[a]-=1
        if degree[a]==0:
          next.append(a)
    if next:
      d.append(next)
def target_check(x,target):
  visited = [0]*(n+1)
  visited[x]=1
  s = graph[x][:]
  while s:
    next = s.pop()
    if next == target:
        return True
    for ne in graph[next]:
      if ne == target:
        return True
      if visited[ne]==0:
        visited[ne]=1
        s.append(ne)
  return False
t = int(input())
for _ in range(t):
  n,k = map(int,input().split())
  times = [0]+list(map(int,input().split()))
  dp = [ [] for _ in range(n+1) ]
  graph = [[] for _ in range(n+1)]
  degree = [0]*(n+1)
  for _ in range(k):
    a,b = map(int,input().split())
    graph[a].append(b)
    degree[b]+=1
  target = int(input())
  topo_sort()
  print(times[target])