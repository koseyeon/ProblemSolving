import sys
input = sys.stdin.readline
n = int(input())
parents = [0]*(n+1)
graph = {}
for i in range(n-1):
    a,b = map(int,input().split())
    if(a not in graph.keys()):
        graph[a] = [b]
    else:
        graph[a].append(b)
    if(b not in graph.keys()):
        graph[b] = [a]
    else:
        graph[b].append(a)
stack = [1]
visited = [0]*(n+1)
visited[1] = 1
while stack:
    parent = stack.pop()
    children = graph[parent]
    for child in children:
        if(visited[child]):
            continue
        parents[child] = parent
        visited[child] = 1
        stack.append(child)
for parent in parents[2:]:
    print(parent)
