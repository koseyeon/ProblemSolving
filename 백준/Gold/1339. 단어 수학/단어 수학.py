from collections import defaultdict
n = int(input())
words = [input() for _ in range(n)]
alpha_dict = defaultdict(int)
for word in words:
    for i in range(len(word)):
        alpha_dict[word[i]] += 10**len(word[i+1:])
alpha_list = list(alpha_dict.items())
alpha_list.sort(key=lambda x:-x[1])
num = 9
num_dict = {}
for i in range(len(alpha_list)):
    num_dict[alpha_list[i][0]] = str(num)
    num -= 1
answer = 0
for word in words:
    temp = ""
    for i in range(len(word)):
        temp += num_dict[word[i]]
    answer += int(temp)
print(answer)

