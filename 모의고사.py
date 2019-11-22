# 11:20

def solution(answers):
    answer = []
    ans_1 = [1,2,3,4,5]
    ans_2 = [2,1,2,3,2,4,2,5]
    ans_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt1, cnt2, cnt3 = 0, 0, 0

    for i in range(0,len(answers)):
        if ans_1[i%len(ans_1)] == answers[i]:
            cnt1 += 1
        if ans_2[i%len(ans_2)] == answers[i]:
            cnt2 += 1
        if ans_3[i%len(ans_3)] == answers[i]:
            cnt3 += 1

    max_n = max([cnt1,cnt2,cnt3])
    print("{},{},{},{}".format(max_n,cnt1,cnt2,cnt3))
    if max_n == cnt1:
        answer.append(1)
    if max_n == cnt2:
        answer.append(2)
    if max_n == cnt3:
        answer.append(3)

    return answer