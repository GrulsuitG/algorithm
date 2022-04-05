# 백준 9461번
import sys

T = int(sys.stdin.readline())

N = []
for i in range(T):
    N.append(int(sys.stdin.readline()))

M = max(N)

memo = [0, 1, 1]


def dp(N):
    for i in range(3, N + 1):
        memo.append(memo[i - 3] + memo[i - 2])


dp(M)
for i in N:
    print(memo[i])
