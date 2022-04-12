# 백준 12865번
import sys

N, K = map(int, sys.stdin.readline().split())

WV = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

WV.sort()
dp = [0] * (K+1)
for w, v in WV:
    for i in range(K, -1, -1):
        if i - w < 0:
            break
        dp[i] = max(dp[i-w] + v, dp[i])

print(dp[K])

# dp = [[0] * (K + 1) for _ in range(N+1)]
#
# for i in range(N + 1):
#     for w in range(K + 1):
#         if i== 0 or w == 0:
#             dp[i][w] == 0
#         elif WV[i-1][0] <= w:
#             dp[i][w] = max(WV[i-1][1] + dp[i-1][w-WV[i-1][0]], dp[i-1][w])
#         else:
#             dp[i][w] = dp[i-1][w]
#
#
# print(dp[N][K])

