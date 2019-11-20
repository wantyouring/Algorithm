A,B = input().split(' ')
A = list(A)
B = list(B)

len_A = len(A)
len_B = len(B)
min = 99999

for i in range(len_B):
    diff_cnt = 0

    for j in range(len_A):
        if i + j >= len_B:
            diff_cnt = 99999 # 여기부터는 계산 x
            break
        if B[i+j] != A[j]:
            diff_cnt += 1
    if min > diff_cnt:
        min = diff_cnt
print(min)
