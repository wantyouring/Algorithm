# 가운데 기준으로 왼쪽인지 오른쪽인지. or 전체 길이 - index 와 index 크기 비교.

N,M = map(int,input().split())
pos = list(map(int,input().split()))
q = [i for i in range(0,N+1)] # 0 ~ N 인덱스까지. 0번 인덱스는 사용 안할거.
result = 0

for num in pos:
    for i in range(len(q)):
        if num == q[i]:
            q_pos = i # 큐에서 해당 수 위치 저장. 절반 위치와 비교하기 위해서.
            break

    # 이동할 필요 없는 경우
    if q_pos == 1:
        q.pop(1)
        continue

    if q_pos >= int(len(q)/2 + 1): # 오른쪽 이동
        # 오른쪽 쭉 회전
        while True:
            result += 1
            q.insert(1,q[-1])
            q.pop(-1)
            if q[1] == num:
                q.pop(1)
                break
    else: # 왼쪽
        while True:
            result += 1
            q.append(q[1])
            q.pop(1)
            if q[1] == num:
                q.pop(1)
                break

print(result)