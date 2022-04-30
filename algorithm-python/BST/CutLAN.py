# 백준 1654번
import sys


def getCount(m):
    return sum(i // m for i in arr)


def findNumber():

    s = 1
    l = arr[-1]
    ans = 0
    while s <= l:
        m = (s + l) // 2
        make = getCount(m)
        if make >= N:
            s = m + 1
            ans = max(ans, m)
        elif make < N:
            l = m - 1

    return ans


K, N = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(K)]
arr.sort()

a = findNumber()
print(a)

