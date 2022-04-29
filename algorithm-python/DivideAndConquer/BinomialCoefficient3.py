# 백준 11401번
import sys

# 정수 a 와 소수 p 에 대해 a^(p-1) % p = 1
#nCk = N! / (N-K)!K!
#    = (N! / (N-K)!K!) * ((N-K)!K!)^(p-1) % p
#    = (N! * ((N-K)!K!)^(p-2) % p
#    = (N! % p * ((N-K)! % p)^(p-2) * (K! % p)^(p-2)) % p
def fact(n):
    r = 1
    for i in range(1, n+1):
        r = (r*i)%R
    return r
def multiple(x, n):
    if n == 1:
        return x % R
    elif n == 2:
        return (x * x) % R
    else:
        if n % 2 == 0:
            return (multiple(x, n // 2) ** 2) % R
        else:
            return ((multiple(x, n // 2) ** 2) * x) % R


N, K = map(int, sys.stdin.readline().split())
R = 1000000007

a = fact(N) % R
b = multiple(fact(N-K), R-2)
c = multiple(fact(K), R-2)

print((a*b*c) % R)

