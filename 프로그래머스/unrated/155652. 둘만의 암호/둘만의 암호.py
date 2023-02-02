def solution(s, skip, index):
    answer = ""
    for i in range(len(s)):
        move = 0
        target = s[i]
        while move < index:
            target = chr(ord(target)+1)
            if ord(target) == ord("z") + 1:
                target = "a"
            if target not in skip:
                move += 1
        answer += target
    return answer
            