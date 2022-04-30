# 백준 1920번
import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
targets = list(map(int, sys.stdin.readline().split()))

arr.sort()


def bst(target):
    s = 0
    l = N - 1
    while s <= l:
        m = (s + l) // 2
        if arr[m] < target:
            s = m + 1
        elif arr[m] > target:
            l = m - 1
        else:
            return 1

    return 0


for target in targets:
    print(bst(target))



