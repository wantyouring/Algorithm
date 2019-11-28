# 9:25 1시간.
global a
a = []
for i in range(12):
    a.append(list(input()))

global visit # 방문했는지 확인용도 global visit
visit = [[False]*6 for _ in range(12)]
dir_i = [-1,1,0,0]
dir_j = [0,0,-1,1]

# 주변 bfs로 터지는지 확인 후 return. input map에 터지는 위치 체크 함수.
def check_bomb(color, map, coor):
    global visit
    global a
    q = []
    v = [[False] * 6 for _ in range(12)]
    cnt = 1
    q.append(coor)
    v[coor[0]][coor[1]] = True

    while len(q) != 0:
        pop_coor = q.pop(0)

        for i in range(4):
            c_i = pop_coor[0] + dir_i[i]
            c_j = pop_coor[1] + dir_j[i]
            if c_i<0 or c_i>11 or c_j<0 or c_j>5:
                continue
            if (map[c_i][c_j] == color and v[c_i][c_j] == False):
                v[c_i][c_j] = True
                q.append((c_i, c_j))
                cnt += 1
                visit[c_i][c_j] = True

    if cnt >= 4:
        for i in range(12):
            for j in range(6):
                if v[i][j]:
                    a[i][j] = 'c' #  폭파될 위치들 저장.
        return True
    else:
        return False


bomb_cnt = 0

bomb_flag = True
while bomb_flag:
    # init variables
    bomb_flag = False
    visit = [[False] * 6 for _ in range(12)]

    # 폭파되는지 체크.
    for i in range(12):
        for j in range(6):
            if a[i][j] != '.' and not visit[i][j]:
                if check_bomb(a[i][j],a,(i,j)):
                    if not bomb_flag:
                        bomb_cnt += 1
                    bomb_flag = True
            else: # .인 경우
                visit[i][j] = True

    # 폭파될 위치 폭파 후 내리기.
    for i in range(12):
        for j in range(6):
            if a[i][j] == 'c': # 폭파할 위치 나오면 위에서부터 당기기.
                for k in range(i,0,-1):
                    a[k][j] = a[k-1][j]
                a[0][j] = '.'
    # print(bomb_cnt)
    # for i in range(12):
    #     print(a[i])
    # print()

print(bomb_cnt)