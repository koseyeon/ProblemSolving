a,b = map(int,input().split())
cul_sum=[0]
k=1
sum_ = 0
while k<=1000:
    for i in range(k):
        sum_ += k
        cul_sum.append(sum_)
    k+=1
print(cul_sum[b]-cul_sum[a-1])