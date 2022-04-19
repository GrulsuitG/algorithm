# 백준 11051
import sys

N, K = map(int, sys.stdin.readline().split())

if K > N / 2:
    K = N - K

result = 1
for i in range(N, N - K, -1):
    result *= i

for i in range(K, 0, -1):
    result //= i

print(result % 10007)