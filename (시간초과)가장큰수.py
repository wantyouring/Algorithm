# 10:56
from itertools import permutations

def solution(numbers):
    answer = ''
    max = 0
    perm = permutations(numbers,len(numbers))
    for ele in perm:
        val = int("".join(map(str,ele)))
        if max < val:
            max = val

    answer = str(max)
    return answer

print(solution([3, 30, 34, 5, 9]))