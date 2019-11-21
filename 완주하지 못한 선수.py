def solution(participant, completion):
    answer = ''
    hash = dict()
    for ele in participant:
        if ele in hash:
            hash[ele] += 1
        else:
            hash[ele] = 1

    for ele in completion:
        if hash[ele] == 1:
            hash.pop(ele)
        else:
            hash[ele] -= 1
    answer = list(hash.keys())[0]
    return answer