# 백준 1655번
import heapq
import sys

N = int(sys.stdin.readline())
minheap = []
maxheap = []
result = []
x = int(sys.stdin.readline())
heapq.heappush(maxheap, (-x, x))
for i in range(1, N):
    result.append(str(maxheap[0][1]))
    x = int(sys.stdin.readline())
    if x > maxheap[0][1]:
        heapq.heappush(minheap, x)
    else:
        heapq.heappush(maxheap, (-x, x))
    if len(maxheap) < len(minheap):
        item = heapq.heappop(minheap)
        heapq.heappush(maxheap, (-item, item))
    elif len(maxheap) - len(minheap) > 1:
        heapq.heappush(minheap, heapq.heappop(maxheap)[1])
result.append(str(maxheap[0][1]))

print('\n'.join(result))

