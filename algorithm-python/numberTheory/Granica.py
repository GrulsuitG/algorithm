# 백준 2981번
import math
import sys

N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(N)]
arr.sort()

gcd = arr[1] - arr[0]
for i in range(2, N):
    gcd = math.gcd(arr[i] - arr[i-1], gcd)

result = []
for i in range(2, int(math.sqrt(gcd)) + 1):
    if gcd % i == 0:
        result.append(i)
        result.append(gcd // i)

result.append(gcd)
result = list(set(result))
result.sort()
print(*map(int, result))

