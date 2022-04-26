# 백준 2164번
import sys

N = int(sys.stdin.readline())
q = [i for i in range(1, N + 1)]

f = 0
b = N-1

while f != b:
    q.append(q[f+1])
    f += 2
    b += 1

print(q[f])

