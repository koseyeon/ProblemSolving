n = int(input())
tree = {}
for _ in range(n):
  node,a,b = input().split()
  tree[node] = [a,b]
def pre_order(tree):
  start = tree['A']
  s = [['A',start]]
  answer = ''
  while s:
    node,[a,b] = s.pop()
    answer+=node
    if b !='.':
      s.append([b,tree[b]])
    if a !='.':
      s.append([a,tree[a]])
  print(answer)
def in_order(tree):
  start = tree['A']
  answer = ''
  s = [['A',start]]
  visited={}
  for node in tree.keys():
    visited[node]=0
  while s:
    node,[a,b] = s[-1]
    if a !='.' and visited[a]==0:
      s.append([a,tree[a]])
      continue
    if a =='.' or visited[a]==1:
      visited[node]=1
      answer += node
      s.pop()
    if b !='.' and visited[b]==0:
      s.append([b,tree[b]])
      continue
  print(answer)
def post_order(tree):
  start = tree['A']
  answer = ''
  s = [['A',start]]
  visited={}
  for node in tree.keys():
    visited[node]=0
  while s:
    node,[a,b] = s[-1]
    if a !='.' and visited[a]==0:
      s.append([a,tree[a]])
      continue
    if b !='.' and visited[b]==0:
      s.append([b,tree[b]])
      continue
    visited[node]=1
    answer += node
    s.pop()
  print(answer)    
pre_order(tree)
in_order(tree)
post_order(tree)