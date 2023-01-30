def solution(k, score):
    answer = []
    board = []
    for i in range(len(score)):
        if len(board) < k:
            board.append(score[i])
            board.sort(reverse=True)
            answer.append(board[-1])
        else:
            board.append(score[i])
            board.sort(reverse=True)
            if(len(board)>k):
                board.pop()
            answer.append(board[-1])
    return answer