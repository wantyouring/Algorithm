def solution(n, lost, reserve):
    answer = 0

    num = [1 for _ in range(n+2)]
    num[0] = 3 # 끝값 indexing 에러 피하기 위해
    num[n+1] = 3
    for ele in reserve:
        num[ele] += 1 # 옷 reserve는 2로.

    for ele in lost:
        num[ele] -= 1

    for i in range(1,n+1):
        if num[i] == 2:
            if num[i-1] == 0:
                num[i] -= 1
                num[i-1] += 1
            elif num[i+1] == 0:
                num[i] -= 1
                num[i+1] += 1

    for i in range(1,n+1):
        if num[i] != 0:
            answer += 1

    return answer

print(solution(5, [2, 4], [1, 3, 5]))