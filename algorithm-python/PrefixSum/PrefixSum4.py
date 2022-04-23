# 백준 11659번
import sys

N, M = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))

memo = [0] * (N+1)
memo[1] = l[0]
for k in range(1, N):
    memo[k+1] = memo[k] + l[k]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    result = memo[j] - memo[i-1]
    print(result)