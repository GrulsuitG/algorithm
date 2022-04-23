# 백준 10986번
# n 번째 항까지의 합을 구한 후  % M 을 한 나머지를 저장해서 나머지가 같은 것들 끼리 골라주면 나머지가 0이 된다
# ex ) 합이 1 3 6 7 9 인 경우  1 7 은  % 3을 할 경우 나머지가 1 그러면 i+1(i == 1) ~ j(j == 4) 를 더 해주면 0이 된다.

import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

memo = [0] * N
dp = [0] * M
memo[0] = arr[0] % M
dp[memo[0]] += 1
for i in range(1, N):
    memo[i] = (memo[i - 1] + arr[i]) % M
    dp[memo[i]] += 1

result = dp[0]
for i in range(M):
    result += dp[i] * (dp[i] - 1) // 2

print(result)


