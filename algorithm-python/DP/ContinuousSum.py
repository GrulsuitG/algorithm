#백준 1912번
import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

dp = [0] * N
for i in range(N):
    dp[i] = max(dp[i-1] + arr[i], arr[i])

print(max(dp))