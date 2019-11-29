n = int(input())
graph = dict()

def add_node(graph,p_node,c_node,w):
    if p_node in graph.keys():
        graph[p_node].append((c_node, w))
    else:
        graph[p_node] = []
        graph[p_node].append((c_node,w))

    if c_node in graph.keys():
        graph[c_node].append((p_node,w))
    else:
        graph[c_node] = []
        graph[c_node].append((p_node,w))

    return graph

for i in range(n-1):
    p_node, c_node, w = map(int,list(input().split()))
    graph = add_node(graph,p_node,c_node,w)

# print(graph)

## 한 node에서 가장 멀리 있는 정점 찾기. 이 점은 지름의 한 정점. 여기서 다시 최대거리 찾기.
# 한 node에서 가장 멀리 있는 정점 찾기.
queue = []
max_len = 0
max_node = 0
queue.append((1,0))
visit = dict()
for ele in graph.keys():
    visit[ele] = False
visit[1] = True
while len(queue)!=0:
    node, total_l = queue.pop(0)
    for ele in graph[node]: #ele:(node,w)
        if visit[ele[0]] == False:
            visit[ele[0]] = True
            if total_l+ele[1] > max_len:
                max_len = total_l+ele[1]
                max_node = ele[0]
            queue.append((ele[0],total_l+ele[1]))

# print(max_len)
# print(max_node)

# 지름의 정점으로부터 최대거리 찾기.
queue = []
max_len = 0
queue.append((max_node,0))
visit = dict()
for ele in graph.keys():
    visit[ele] = False
visit[max_node] = True
while len(queue)!=0:
    node, total_l = queue.pop(0)
    for ele in graph[node]: #ele:(node,w)
        if visit[ele[0]] == False:
            visit[ele[0]] = True
            if total_l+ele[1] > max_len:
                max_len = total_l+ele[1]
                max_node = ele[0]
            queue.append((ele[0],total_l+ele[1]))

print(max_len)
# print(max_node)