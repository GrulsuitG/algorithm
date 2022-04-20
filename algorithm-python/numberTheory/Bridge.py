#백준 1010번
import math
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    print(math.comb(M,N))