T = int(input())

for t in range(T):
    N,M = map(int,input().split())
    q = list(map(int,input().split()))
    index = [i for i in range(len(q))] # 처음 index 가르키는 리스트
    cnt = 0
    prt_i = 9999 # 초기화 필요

    while True:
        flag = True
        # 나보다 큰 거 있는지
        for i in range(1,len(q)):
            if q[0] < q[i]:
                flag = False

        if flag:
            cnt += 1
            prt_i = index[0]
            q.pop(0)
            index.pop(0)
        else:
            q.append((q[0]))
            q.pop(0)
            index.append(index[0])
            index.pop(0)


        if prt_i == M:
            print(cnt)
            break