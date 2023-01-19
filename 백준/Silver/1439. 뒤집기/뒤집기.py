s = input()
prev = s[0]

one = 0
zero = 0
for i in range(1,len(s)):
  if prev == "1" and s[i] == "0":
    one += 1
    prev = "0"
  elif prev == "0" and s[i] == "1":
    zero += 1
    prev = "1"
if prev == "1" and s[-1] == "1":
  one += 1
elif prev == "0" and s[-1] == "0":
  zero += 1
print(min(one,zero))

  
