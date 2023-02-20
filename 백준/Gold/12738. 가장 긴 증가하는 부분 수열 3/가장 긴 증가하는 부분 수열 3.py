def binary_search(K,x):
    s,e = 0,len(K)-1
    while s<=e:
        mid = (s+e)//2
        if K[mid] == x:
            return mid
        elif K[mid] < x:
            s = mid+1
            continue
        else:
            e = mid-1
            continue
    return s
N = int(input())
A = list(map(int,input().split()))
K = [A[0]]
for i in range(1,N):
    if K[-1] < A[i]:
        K.append(A[i])
    else:
        idx = binary_search(K,A[i])
        K[idx] = A[i]
print(len(K))