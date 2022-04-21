#백준 11985번

import sys

N, M, K = map(int, sys.stdin.readline().split())
orange = [0] + [int(sys.stdin.readline()) for _ in range(N)]

dp = [0] * (N+1)
dp[1] = K
for i in range(2, N+1):
    _min = _max = orange[i]

    bound = min(i, M) + 1
    dp[i] = dp[i-1] + K

    for size in range(2, bound):
        j = i - size + 1
        _min = min(_min, orange[j])
        _max = max(_max, orange[j])

        cost = K + size * (_max - _min)

        dp[i] = min(dp[i], dp[j - 1] + cost)

print(dp[N])

