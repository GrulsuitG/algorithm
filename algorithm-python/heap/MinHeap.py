# 백준 1927번
import heapq
import sys

N = int(sys.stdin.readline())
h = []

result = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(h) == 0:
            result.append('0')
        else:
            result.append(str(heapq.heappop(h)))
    else:
        heapq.heappush(h, x)

print('\n'.join(result))