# 백준 1676번
import sys

N = int(sys.stdin.readline())

cnt = [0, 0]
for i in range(1, N+1):
    while True:
        if i % 2 == 0:
            cnt[0] += 1
            i = i // 2
        elif i % 5 == 0:
            cnt[1] += 1
            i = i // 5
        else:
            break

print(min(cnt))
