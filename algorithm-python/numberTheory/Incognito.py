# 백준 9375번
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    itemNumber = {}
    for _ in range(N):
        _, kind = sys.stdin.readline().split()
        if kind not in itemNumber:
            itemNumber[kind] = 1
        else:
            itemNumber[kind] += 1

    result = 1
    for item in itemNumber:
        result *= (itemNumber[item] + 1)

    print(result - 1)
