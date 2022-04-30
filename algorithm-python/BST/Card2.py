# 백준 10816번
import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
targets = list(map(int, sys.stdin.readline().split()))

count = {}

for i in arr:
    if count.get(i):
        count[i] += 1
    else:
        count[i] = 1

result = []

for target in targets:
    num = count.get(target)
    if num:
        result.append(str(num))
    else:
        result.append('0')

print(' '.join(map(str, result)))
