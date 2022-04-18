# 백준 1934번
import sys

N = int(sys.stdin.readline())


def getGcd(m, n):
    if m < n:
        m, n = n, m
    if n == 0:
        return m
    elif m % n == 0:
        return n
    else:
        return getGcd(n, m % n)


for i in range(N):
    m, n = map(int, sys.stdin.readline().split())
    gcd = getGcd(m, n)
    print(gcd * (m // gcd) * (n // gcd))
