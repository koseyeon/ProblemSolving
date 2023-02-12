from collections import defaultdict
def solution(genres, plays):
    answer = []
    genres_dict = defaultdict(lambda:[0,[]])
    for i in range(len(genres)):
        genres_dict[genres[i]][0] += plays[i]
        genres_dict[genres[i]][1].append([plays[i],i])
    g_list = sorted(list(genres_dict.values()),key=lambda x:-x[0])
    for i in range(len(g_list)):
        songs = sorted(g_list[i][1],key=lambda x:(-x[0],x[1]))
        for j in range(min(2,len(songs))):
            answer.append(songs[j][1])
    return answer