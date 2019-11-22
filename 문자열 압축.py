def solution(s):
    answer = 0

    len_s = len(s)
    s = list(s)
    min = 1005

    if len_s == 1:
        min = 1

    for cut in range(1,int(len_s/2)+1):
        result_s = []
        save_s = []
        cnt_s = []

        for i in range(0,len_s,cut):
            save_s.append(s[i:i+cut])

        cnt = 1
        for i in range(len(save_s)-1):
            if save_s[i] == save_s[i+1]:
                cnt += 1
            else:
                cnt_s.append([cnt,save_s[i]])
                cnt = 1
            if i == (len(save_s) - 2):
                cnt_s.append([cnt,save_s[i+1]])

        for ele in cnt_s:
            if ele[0] == 1:
                result_s.extend(ele[1])
            else:
                result_s.extend(list(str(ele[0])))
                result_s.extend(ele[1])

        if min > len(result_s):
            min = len(result_s)

        # print(result_s)

    answer = min
    return answer

print(solution("aaaaabbb"))