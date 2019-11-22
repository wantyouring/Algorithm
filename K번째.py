# 10:48

def solution(array, commands):
    answer = []

    arr = array
    for ele in commands:
        arr = array[ele[0]-1:ele[1]]
        arr = sorted(arr)
        answer.append(arr[ele[2]-1])

    return answer

