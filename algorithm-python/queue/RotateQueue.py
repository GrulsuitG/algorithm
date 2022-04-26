# 백준 1021번
import sys

N, M = map(int, sys.stdin.readline().split())
target = list(map(int, sys.stdin.readline().split()))

arr = [i for i in range(1, N+1)]

times = 0
idx = 0
for t in target:
    if arr[idx] == target:
        arr.pop(idx)
    else:
        target_idx = 0
        for i in range(len(arr)):
            if arr[i] == t:
                target_idx = i
                break
        times += min(abs(target_idx - idx), len(arr) - abs(target_idx - idx))
        idx = target_idx
        arr.pop(target_idx)
        if idx == len(arr):
            idx = 0

print(times)