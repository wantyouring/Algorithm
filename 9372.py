def bfs(graph, start_node):
    visit = list()
    queue = list()
    cnt = 0

    queue.append(start_node)

    while queue:
        node = queue.pop(0)

        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])

    return cnt

# # 입력
# N,M = map(int,input().split())
#
# # graph 초기화
# graph = dict()
# for i in range(1,N+1):
#     graph[i] = set()
#
# # graph 작성
# for i in range(M):
#     a,b = map(int,input().split()) # 입력
#     graph[a].add(b)
#     graph[b].add(a)
#
# # print(graph)
import sys

T = int(sys.stdin.readline().rstrip())
for t in range(T):
    N, M = map(int, sys.stdin.readline().rstrip().split())
    for i in range(M):
        a, b = map(int, sys.stdin.readline().rstrip().split())  # 입력
    print(N-1)
