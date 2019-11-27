def solution(N):
    answer = 0
    a = []
    if N==1 or N==2:
        return 1
    a.append(1)
    a.append(1)

    for i in range(2,N+1):
        a.append(a[i-1] + a[i-2])
    answer = (a[N-1] + a[N])*2

    return answer

print(solution(5))