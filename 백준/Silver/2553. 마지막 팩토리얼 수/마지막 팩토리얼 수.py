n = int(input())
ans = 1
for i in range(n,1,-1):
    ans *= i
ans = str(ans)
for i in range(len(ans)-1,-1,-1):
    if ans[i]!='0':
        print(ans[i])
        break