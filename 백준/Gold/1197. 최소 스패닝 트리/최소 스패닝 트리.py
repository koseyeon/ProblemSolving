def find_parent(parent,x):
  if parent[x] != x:
    parent[x]=find_parent(parent,parent[x]) 
  return parent[x]
def union_parent(parent,a,b):
  a = find_parent(parent,a)
  b = find_parent(parent,b)
  if a<b:
    parent[b]=a
  else:
    parent[a]=b
v,e = map(int,input().split())
parent = [0]*(v+1)
for i in range(1,v+1):
  parent[i]=i
edges = []
for _ in range(e):
  edges.append(list(map(int,input().split())))
edges.sort(key=lambda x : x[2])
ans = 0
for ed in edges:
  a,b,c = ed
  if find_parent(parent,a) == find_parent(parent,b):
    continue
  else:
    union_parent(parent,a,b)
    ans+=c
print(ans)