# 백준 11066번
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    K = int(sys.stdin.readline())
    size = list(map(int, sys.stdin.readline().split()))
    memo = [[0] * K for _ in range(K)]

    for i in range(K - 1):
        memo[i][i + 1] = size[i] + size[i + 1]
        for j in range(i + 2, K):
            memo[i][j] = memo[i][j - 1] + size[j]

    for d in range(2, K):
        for i in range(K - d):
            j = i + d
            minimum = [memo[i][k] + memo[k + 1][j] for k in range(i, j)]
            memo[i][j] += min(minimum)

    print(memo[0][K - 1])
