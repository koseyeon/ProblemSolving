# 매번 그 순간에 가장 큰 숫자에 가장 작은 숫자가 곱해지도록 하자.
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.sort()
B.sort(reverse=True)
s = 0
for i in range(N):
    s += A[i]*B[i]
print(s)