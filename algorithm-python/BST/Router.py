# 백준 2110번
import sys

N, C = map(int, sys.stdin.readline().split())
houses = [int(sys.stdin.readline()) for _ in range(N)]
houses.sort()

s = 1
e = houses[-1] - houses[0]
ans = houses[-1] - houses[0]
while s <= e:
    m = (s + e) // 2

    prev = houses[0]
    cnt = 1
    for i in range(1, N):
        if houses[i] - prev >= m:
            cnt += 1
            prev = houses[i]

    if cnt >= C:
        ans = m
        s = m + 1
    else:
        e = m - 1

print(ans)