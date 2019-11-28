# 10:40
'''
7 8 1
0 0 0 0 0 0 0 9
5 0 0 0 3 0 0 8
-1 0 5 0 0 0 22 0
-1 8 0 0 0 0 0 0
5 0 0 0 0 10 43 0
0 0 5 0 15 0 0 0
0 0 40 0 0 0 20 0
'''

R,C,T = map(int,input().split())
board = []
cleaner_top = 0
cleaner_bot = 0
di = [0,0,-1,1]
dj = [-1,1,0,0]

for i in range(R):
    board.append(list(map(int,list(input().split()))))
# 공기청정기 찾기.
for i in range(R):
    if board[i][0] == -1:
        cleaner_top = i
        cleaner_bot = i+1
        break

new_board = [[0]*C for _ in range(R)]
for i in range(R):
    for j in range(C):
        new_board[i][j] = board[i][j]

while T>0:
    T-=1
    for i in range(R):
        for j in range(C):
            board[i][j] = new_board[i][j]
    # 미세먼지 확산.
    for i in range(R):
        for j in range(C):
            if board[i][j] == -1:
                continue
            # 4방향 확산.
            for k in range(4):
                move_i = i+di[k]
                move_j = j+dj[k]
                if move_i<0 or move_i>R-1 or move_j<0 or move_j>C-1 or \
                        (move_i==cleaner_top and move_j==0) or (move_i==cleaner_bot and move_j==0):
                    continue
                else:
                    new_board[move_i][move_j] += board[i][j]//5
                    new_board[i][j] -= board[i][j]//5

    # 청정기 돌리기
    # 위 공기청정기.
    for i in range(cleaner_top-1,0,-1):
        new_board[i][0] = new_board[i-1][0]
    for i in range(C-1):
        new_board[0][i] = new_board[0][i+1]
    for i in range(cleaner_top):
        new_board[i][C-1] = new_board[i+1][C-1]
    for i in range(C-2,0,-1):
        new_board[cleaner_top][i+1] = new_board[cleaner_top][i]
    new_board[cleaner_top][1] = 0

    # 아래 공기청정기. 7->6, 6->5
    for i in range(cleaner_bot+1,R-1):
        new_board[i][0] = new_board[i+1][0]
    for i in range(C-1):
        new_board[R-1][i] = new_board[R-1][i+1]
    for i in range(R-1,cleaner_bot,-1):
        new_board[i][C-1] = new_board[i-1][C-1]
    for i in range(C-2,0,-1):
        new_board[cleaner_bot][i+1] = new_board[cleaner_bot][i]
    new_board[cleaner_bot][1] = 0

    for i in range(R):
        for j in range(C):
            board[i][j] = new_board[i][j]

sum = 0
for i in range(R):
    for j in range(C):
        if new_board[i][j] != -1:
            sum += new_board[i][j]

print(sum)