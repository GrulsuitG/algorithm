# 백준 2609번
import sys

N, M = map(int, sys.stdin.readline().split())

gcd = 1

for i in range(1, N + 1):
    if N % i == 0 and M % i == 0:
        gcd = i

a = N // gcd
b = M // gcd

lcm = gcd * a * b
print(gcd)
print(lcm)