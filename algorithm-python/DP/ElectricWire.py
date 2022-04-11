# 백준 2565번
import sys

N = int(sys.stdin.readline())

pole = {}
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    pole[a] = b


key = list(map(int, pole.keys()))
key.sort()

pattern = []
for i in key:
    pattern.append(pole[i])


arr = [pattern[0]]

for i in range(1, N):
    target = pattern[i]

    if target > arr[-1]:
        arr.append(target)
    else:
        s = 0
        l = len(arr)

        while s < l:
            m = (s + l) // 2
            if arr[m] > target:
                l = m
            else:
                s = m + 1

        arr[l] = target

print(N - len(arr))

