def solution(n, edge):
    answer = 0
    graph = dict()

    # 1 node로부터 거리값 저장
    d = [0 for _ in range(n+1)]

    # graph 초기화
    for i in range(1,n+1):
        graph[i] = []

    # node들 graph에 추가하기.
    for ele in edge:
        if ele[1] not in graph[ele[0]]:
            graph[ele[0]].append(ele[1])
        if ele[0] not in graph[ele[1]]:
            graph[ele[1]].append(ele[0])

    # queue로 bfs 돌며 1 node로부터 거리 저장
    queue = []
    queue.append(1)
    while len(queue) != 0:
        node = queue.pop(0)
        for ele in graph[node]:
            if d[ele] == 0 and ele != 1:
                d[ele] = d[node] + 1
                queue.append(ele)

    max_d = max(d)
    for i in range(2,n+1):
        if d[i] == max_d:
            answer += 1

    return answer

print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))