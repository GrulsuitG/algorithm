# 백준 11399
import sys

N = int(sys.stdin.readline())

# waitTime = sorted(list(map(int, sys.stdin.readline().split())))
waitTime = list(map(int, sys.stdin.readline().split()))
waitTime.sort()

# total = sum(waitTime[i] * (N - i) for i in range(N))
total = 0
for i in range(N):
    total += waitTime[i] * (N - i)

print(total)