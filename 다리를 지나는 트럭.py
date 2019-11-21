def solution(bridge_length, weight, truck_weights):
    answer = 0

    sum = 0
    queue = [0 for _ in range(bridge_length)]
    t = 0

    while queue:
        sum -= queue.pop(0)
        t += 1
        if len(truck_weights) > 0:
            if sum + truck_weights[0] <= weight: # 적재 가능
                sum += truck_weights[0]
                queue.append(truck_weights[0])
                truck_weights.pop(0)
            else:
                queue.append(0)

    answer = t

    return answer