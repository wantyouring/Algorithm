import sys
# 그냥 input으로 받으면 시간초과
N = int(sys.stdin.readline().rstrip())
sum = 0

for i in range(N):
    sum += int(sys.stdin.readline().rstrip())
print(sum + 1 - N)