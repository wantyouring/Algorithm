# 3:20~

r,c,k = map(int,list(input().split()))
A = []
for i in range(3):
    A.append(list(map(int,list(input().split()))))
# print(len(A))

def sort_save(arr):
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i][1] > arr[j][1] or (arr[i][1] == arr[j][1] and arr[i][0] > arr[j][0]):
                t = arr[i]
                arr[i] = arr[j]
                arr[j] = t
    return arr

def r_calc(A,row):
    hash = [0] * 101
    save = []
    # row행 해싱.
    for j in range(len(A[row])):
        hash[A[row][j]] += 1
    # 나온 숫자, 횟수 저장.
    for i in range(1,101):
        if hash[i] != 0:
            save.append((i,hash[i])) # (숫자, 횟수)

    save = sort_save(save)

    # A 해당 row 연산 후로 바꾸기.
    A[row] = []
    for i in range(len(save)):
        if i>=50: # 100개 까지.
            break
        A[row].append(save[i][0])
        A[row].append(save[i][1])

    return A

for ans in range(0,102):
    r_num = len(A)
    c_num = len(A[0])

    if ans==101:
        print(-1)
        break
    elif r_num <= r-1 or c_num <= c-1: # 처음 준 좌표보다 더 작아지는 경우.
        ans += 1
    elif A[r-1][c-1] == k:
        print(ans)
        break
    else:
        ans += 1

    # R연산
    if r_num >= c_num:
        for i in range(r_num):
            r_calc(A,i)
        # c_num에 최대길이 넣기.
        max = 0
        for i in range(r_num):
            if len(A[i]) > max:
                max = len(A[i])
        c_num = max

        # 빈 공간 0으로 채우기.
        for i in range(r_num):
            if len(A[i]) < c_num:
                for j in range(c_num - len(A[i])):
                    A[i].append(0)
        # print(A)
    elif r_num < c_num:
        ## 전치행렬 취한 뒤 r_calc 똑같이 진행 후 다시 전치행렬 취하기.
        # 전치행렬 취하기.
        new_A = [[0]*r_num for _ in range(c_num)]
        for i in range(r_num):
            for j in range(c_num):
                new_A[j][i] = A[i][j]

        # r_calc 진행.
        new_r = c_num
        new_c = r_num
        # print(new_r)
        # print(new_c)

        for i in range(new_r):
            r_calc(new_A,i)

        max = 0
        for i in range(new_r):
            if len(new_A[i]) > max:
                max = len(new_A[i])
        new_c = max

        # 빈 공간 0으로 채우기.
        for i in range(new_r):
            if len(new_A[i]) < new_c:
                for j in range(new_c - len(new_A[i])):
                    new_A[i].append(0)

        # for i in range(len(new_A)):
        #     print(new_A[i])
        # print()
        # print(new_r)
        # print(new_c)

        # 다시 전치행렬 취하기
        A = [[0]*new_r for _ in range(new_c)]
        for i in range(new_r):
            for j in range(new_c):
                A[j][i] = new_A[i][j]

        # print(A)
