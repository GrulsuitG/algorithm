# 백준 1904번
import sys

N = int(sys.stdin.readline())

memo = [1, 1, 2]
const = 15746

def dp(N):
    for i in range(3, N+1):
        result = memo[i-2]+memo[i-1]
        result %= const
        memo.append(result)

dp(N)
print(memo[N])
