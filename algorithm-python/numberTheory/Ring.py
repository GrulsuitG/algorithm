# 백준 3036번
import sys

N = int(sys.stdin.readline())
radius = list(map(int, sys.stdin.readline().split()))

def gcd(m, n):
    if m < n:
        m, n = n, m
    if n == 0:
        return m
    elif m % n == 0:
        return n
    else:
        return gcd(n, m % n)

def lcm(m, n):
    g = gcd(m, n)
    a, b = m // g, n //g
    return g * a * b

for i in range(1, N):
    l = lcm(radius[0], radius[i])


    a = l // radius[i]
    b = l // radius[0]
    print("%d/%d" % (a, b))

