# 백준 11047번
import sys

N, K = map(int, sys.stdin.readline().split())

coin = [int(sys.stdin.readline()) for _ in range(N)]

result = 0
for i in range(N-1, -1, -1):
    target = K // coin[i]

    if target != 0:
        result += target
        K -= target * coin[i]

print(result)