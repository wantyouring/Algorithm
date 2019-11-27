# queue 모듈로 시간초과. heapq module 사용해야했음.

# from queue import PriorityQueue
import heapq

def solution(scoville, K):
    answer = 0
    # queue= PriorityQueue()
    heap = []
    for ele in scoville:
        heapq.heappush(heap,ele)
        # queue.put(ele)

    while len(heap) > 1:
        a = heapq.heappop(heap)
        if a >= K:
            break
        b = heapq.heappop(heap)
        heapq.heappush(heap,a+2*b)
        answer += 1

        # a = queue.get()
        # if a >= K:
        #     break
        # b = queue.get()
        # queue.put(a + 2*b)
        # answer += 1
    if len(heap) == 1:
        if heapq.heappop(heap) < K:
            return -1

    # if queue.qsize() == 1:
    #     if queue.get() < K:
    #         return -1

    return answer

print(solution([1, 2],7))