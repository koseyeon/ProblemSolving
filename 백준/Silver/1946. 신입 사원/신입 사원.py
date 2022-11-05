import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
  n = int(input())
  doc_order = []
  for _ in range(n):
    a,b = map(int,input().split())
    doc_order.append([a,b])
  doc_order.sort(key=lambda x:x[0])
  cnt = n
  interview_top = doc_order[0][1]
  for i in range(1,n):
    interview_rank = doc_order[i][1]
    if interview_top > interview_rank:
      interview_top = interview_rank
    else:
      cnt-=1
  print(cnt)