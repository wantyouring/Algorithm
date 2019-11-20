# board크기 입력받아 몇 개 고쳐야하는지 return
def func(board):
    start_c = board[0][0]
    cnt = 0
    for i in range(8):
        for j in range(8):
            if (i+j)%2 == 0:
                if board[i][j] == start_c:
                    continue
                else:
                    cnt += 1
            else:
                if board[i][j] == start_c:
                    cnt += 1
                else:
                    continue
    # start_c 바꿔서
    if start_c == 'B':
        start_c = 'W'
    else:
        start_c = 'B'

    cnt2 = 0

    for i in range(8):
        for j in range(8):
            if (i+j)%2 == 0:
                if board[i][j] == start_c:
                    continue
                else:
                    cnt2 += 1
            else:
                if board[i][j] == start_c:
                    cnt2 += 1
                else:
                    continue
    if cnt > cnt2:
        cnt = cnt2
    return cnt

N,M = map(int,input().split())
board = []
for i in range(N):
    board.append(list(input()))

min = 100000000
for i in range(0,N):
    for j in range(0,M):
        if i+8 > N or j+8 > M:
            continue
        tmp_board = [] # numpy 못 써서 list slicing으로
        for k in range(8):
            tmp_board.append(board[i+k][j:j+8])
        tmp = func(tmp_board)
        if min > tmp:
            min = tmp
print(min)
