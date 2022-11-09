target_str = input()
bomb = input()
stack = []
def check():
  len_s = len(stack)
  len_b = len(bomb)
  if len_s < len_b:
    return
  for i in range(len_b):
    if stack[len_s-len_b+i]!=bomb[i]:
      return
  for i in range(len_b):
    stack.pop()
for i in range(len(target_str)):    
  stack.append(target_str[i])
  check()
if len(stack)==0:
  print("FRULA")
else:
  print("".join(stack))