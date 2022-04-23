# 백준 2559번
import sys

N, K = map(int, sys.stdin.readline().split())

temperature = list(map(int, sys.stdin.readline().split()))

M = sum(temperature[:K])
result = M
for i in range(K, N):
    M = M - temperature[i - K] + temperature[i]
    result = max(M, result)

print(result)