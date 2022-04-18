# 백준 1037번
import sys

N = int(sys.stdin.readline())

factor = list(map(int, sys.stdin.readline().split()))

print(min(factor) * max(factor))