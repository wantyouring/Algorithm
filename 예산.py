def solution(budgets, M):
    answer = 0

    def calc(budgets,lim):
        sum = 0
        for ele in budgets:
            if ele <= lim:
                sum += ele
            else:
                sum += lim
        return sum

    s = 1
    e = max(budgets)+1
    while True:
        m = int((s+e)/2)
        res = calc(budgets,m)
        if res == M or s == m or e == m:
            res = calc(budgets,e) # e 끝 값이 가능한 경우 계산.
            if e > max(budgets):
                return max(budgets) # 최댓값보다 큰 경우는 최댓값 return
            if res < M:
                answer = e
            else:
                answer = m
            break
        elif res > M:
            e = m
        elif res < M:
            s = m

    return answer

# print(solution([120, 110, 140, 150],485))
print(solution([2,2,2],7))