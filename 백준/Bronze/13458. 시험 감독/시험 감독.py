import sys,math
input = sys.stdin.readline
n = int(input())
nums = list(map(int,input().split()))
b,c = map(int,input().split())
answer = 0
for nu in nums:
  if nu>b:
    answer += 1
    answer += math.ceil((nu-b)/c)
  else:
    answer+=1
print(answer)