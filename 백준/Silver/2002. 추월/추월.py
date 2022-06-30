n = int(input())
in_dict = {}
out_list = []
for i in range(n):
    in_dict[input()] = i
for i in range(n):
    car_num = input()
    out_list.append(in_dict[car_num])
ans = 0
for i in range(n):
    for j in range(i+1,n):
        if out_list[i]>out_list[j]:
            ans+=1
            break
print(ans)