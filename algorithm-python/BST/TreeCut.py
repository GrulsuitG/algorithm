# 백준 2805번
import sys
from collections import Counter

N, M = map(int, sys.stdin.readline().split())
trees = Counter(map(int, sys.stdin.readline().split()))
s = 1
e = max(trees)

while s <= e:
    m = (s + e) // 2
    total = sum((h - m) * i for h, i in trees.items() if h > m)
    if total >= M:
        s = m + 1
    elif total < M:
        e = m - 1

print(e)



