s = list(input())
i = 0
l = len(s)
while i<l:
    if s[i]=='<':
        for j in range(i,l):
            if s[j] == '>':
                break
        i = j+1
        continue
    else:
        temp = []
        next = 0
        for j in range(i,l):
            if s[j] == " ":
                next = j+1
                break
            elif s[j] == "<":
                next = j
                break
            temp.append(s[j])
        for j in range(i,i+len(temp)):
            s[j]=temp.pop()
        if next == 0:
            break
        i = next
ans = ""
for a in s:
    ans+=a
print(ans)


