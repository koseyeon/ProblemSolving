def solution(s):
    answer = True
    stack = []
    for i in range(len(s)):
        if s[i] == ")":
            if stack:
                stack.pop()
            else:
                return False
        else:
            stack.append(s[i])
    if stack:
        return False
    else:
        return True