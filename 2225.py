N,K = map(int,input().split())

dp = [[0 for j in range(K+1)] for i in range(N+1)]

for k in range(1,K+1):
    for n in range(1,N+1):
        if k==1:
            dp[n][k] = 1
            continue
        if n==1:
            dp[n][k] = k
            continue

        for i in range(1,n+1):
            dp[n][k] += dp[i][k-1]
        dp[n][k] += 1
        dp[n][k] %= 1000000000
# print(dp)
print(dp[n][k] % 1000000000)

