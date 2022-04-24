# 백준 11660번
import sys

N, M = map(int, sys.stdin.readline().split())

table = [[0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    table[i][1:] = list(map(int, sys.stdin.readline().split()))
    for j in range(1, N+1):
        table[i][j] += table[i][j-1] + table[i-1][j] - table[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    result = table[x2][y2] - table[x1-1][y2] - table[x2][y1-1] + table[x1-1][y1-1]
    print(result)

