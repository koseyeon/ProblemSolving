t1 = list(input())
t2 = list(input())
t3 = list(input())
t4 = list(input())
t_list = [[],t1,t2,t3,t4]
k = int(input())
def rotate(num,direction):
  visited[num] = 1
  if num == 1:
    if(t_list[num][2] != t_list[num+1][6] and not visited[num+1]):
      rotate(num+1,-direction)
  elif 2<=num<=3:
    if(t_list[num][6] != t_list[num-1][2] and not visited[num-1]):
      rotate(num-1,-direction)
    if(t_list[num][2] != t_list[num+1][6] and not visited[num+1]):
      rotate(num+1,-direction)
  else:
    if(t_list[num][6] != t_list[num-1][2] and not visited[num-1]):
      rotate(num-1,-direction)
  if direction == 1:
    t_list[num] = [t_list[num][-1]] + t_list[num][0:-1]
  else:
    t_list[num] = t_list[num][1:] + [t_list[num][0]]
for _ in range(k):
  a,b = map(int,input().split())
  visited = [0]*5
  rotate(a,b)
answer = 0
for i in range(1,5):
  answer += int(t_list[i][0])*((2)**(i-1))
print(answer)