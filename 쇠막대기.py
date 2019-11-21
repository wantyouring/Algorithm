def solution(arrangement):
    answer = 0
    stack = 0

    arrangement = list(arrangement)
    for i in range(len(arrangement)):
        if arrangement[i] == '(':
            stack += 1
        else:
            if arrangement[i-1] == '(': # 레이저
                stack -= 1
                answer += stack
            else:
                answer += 1
                stack -= 1

    return answer

