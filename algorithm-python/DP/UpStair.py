# 백준 2579번
import sys

N = int(sys.stdin.readline())

stair = [0]
for _ in range(N):
    stair.append(int(sys.stdin.readline()))

if N == 1:
    print(stair[N])
else:
    memo = [[0, 0] for _ in range(N + 1)]

    for i in range(N + 1):
        # i 번째를 1계단으로 오르려면 i-1 번째를 두계단으로 올라온상태
        memo[i][0] = memo[i - 1][1] + stair[i]
        # i 번째를 2계단으로 오르려면 i-2번째를 한계단 혹은 두계단 으로 올라온 상태
        memo[i][1] = max(memo[i - 2]) + stair[i]

    print(max(memo[N]))
