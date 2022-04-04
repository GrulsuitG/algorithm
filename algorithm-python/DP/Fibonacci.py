# 백준 1003번
import sys

T = int(sys.stdin.readline())

memo = {0: [1, 0], 1: [0, 1]}


def dp(N):
    if N == 0:
        return memo[0]
    elif N == 1:
        return memo[1]
    else:
        if memo.get(N) is None:
            time = [i + j for i,j in zip(dp(N - 1), dp(N - 2))]
            memo[N] = time
        return memo[N]


N = [int(sys.stdin.readline()) for _ in range(T)]
for i in N:
    result = dp(i)
    print(result[0], result[1])
