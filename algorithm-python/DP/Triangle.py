# 백준 1932번
import sys

N = int(sys.stdin.readline())

Triangle = []
for _ in range(N):
    Triangle.append(list(map(int, sys.stdin.readline().split())))

for line in range(1, N):
    Triangle[line][0] += Triangle[line - 1][0]
    for i in range(1, line):
        # print(i)
        Triangle[line][i] += max(Triangle[line-1][i], Triangle[line-1][i-1])
    Triangle[line][line] += Triangle[line-1][line-1]

print(max(Triangle[N-1]))