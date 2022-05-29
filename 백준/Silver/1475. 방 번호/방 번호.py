import math
n = input()
counts = [0]*10
for i in range(10):
    if i==6:
        counts[9] += n.count(str(i))
    else:
        counts[i] += n.count(str(i))
counts[9] = math.ceil(counts[9]/2)
print(max(counts))