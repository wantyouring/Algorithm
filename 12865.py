# dp문제 미해결.

N,K = map(int,list(input().split()))
objs = []
dp = [0]*(K+1)

for i in range(N):
    W, V = map(int, list(input().split()))
    objs.append((W,V))

for i in range(N):
    for j in range(K,0,-1):
        if j + objs[i][0] > K:
            continue

        if dp[j - objs[i][0]] + objs[i][1] > dp[j]:
            dp[j] = dp[j - objs[i][0]] + objs[i][1]
    print(dp)

#중복 제거하기.
print(dp)
print(dp[K])