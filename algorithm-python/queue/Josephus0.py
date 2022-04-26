# 백준 11866번
import sys

N, K = map(int, sys.stdin.readline().split())
num = [i for i in range(1, N + 1)]
result = []
idx = 0

while num:
    idx = (idx + K - 1) % (len(num))
    result.append(num.pop(idx))

print('<' + ', '.join(map(str, result)) + '>')
