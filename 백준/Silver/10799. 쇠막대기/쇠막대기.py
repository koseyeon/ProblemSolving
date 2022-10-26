arr = input()
s = []
cnt = 0
prev = '('
for now in arr:
    if now == '(' and prev == '(':
        s.append(now)
    elif now == '(' and prev == ')':
        s.append(now)
        prev = '('
    elif now == ')' and prev == '(':
        s.pop()
        cnt+=len(s)
        prev = ')'
    else:
        s.pop()
        cnt += 1
print(cnt)