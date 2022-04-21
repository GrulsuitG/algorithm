# 백준 2004번
import sys

N, M = map(int, sys.stdin.readline().split())


def count(i, j):
    cnt = 0
    while i:
        i //= j
        cnt += i
    return cnt


two = count(N, 2) - count(M, 2) - count(N - M, 2)
five = count(N, 5) - count(M, 5) - count(N - M, 5)

print(min(two, five))
