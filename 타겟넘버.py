# 11:36

def solution(numbers, target):
    global answer
    answer = 0

    numbers
    # pm = [False for i in range(len(numbers))] # True : +, False : -
    pm = [False]*len(numbers)

    def recur(idx,pm,numbers,target):
        global answer
        if idx > len(numbers)-1:
            # print(pm)
            sum = 0
            for i in range(len(numbers)):
                if pm[i]:
                    sum += numbers[i]
                else:
                    sum -= numbers[i]
            if target == sum:
                answer += 1
            return

        pm[idx] = False
        recur(idx+1,pm,numbers,target)
        pm[idx] = True
        recur(idx+1,pm,numbers,target)

    recur(0,pm,numbers,target)

    return answer

print(solution([1, 1, 1, 1, 1],3))