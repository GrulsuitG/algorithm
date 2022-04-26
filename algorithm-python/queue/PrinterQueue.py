# 백준 1966
import sys

T = int(sys.stdin.readline())

result = []
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))

    idx = 1
    target_idx = M
    while True:
        if arr[0] < max(arr):
            if target_idx == 0:
                target_idx = len(arr) - 1
            else:
                target_idx -= 1
            arr.append(arr.pop(0))

        elif arr[0] == max(arr):
            if target_idx == 0:
                result.append(idx)
                break
            arr.pop(0)
            idx += 1
            target_idx -= 1

print('\n'.join(map(str, result)))