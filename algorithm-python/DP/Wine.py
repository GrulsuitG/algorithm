# 백준 2156번
import sys

N = int(sys.stdin.readline())

wine = []
for _ in range(N):
    wine.append(int(sys.stdin.readline()))

if N < 3:
    print(sum(wine))

else:
    # 연속으로 마신 경우 / 한 칸 뛰고 마신 경우 / 두 칸 뛰고 마신 경우
    memo = [[0, 0, 0] for _ in range(N)]
    memo[0] = [wine[0], wine[0], wine[0]]
    memo[1] = [wine[0] + wine[1], wine[1], wine[1]]
    memo[2] = [wine[1] + wine[2], wine[0] + wine[2], wine[2]]
    for i in range(3, N):
        # _OXXO
        memo[i][2] = max(memo[i - 3]) + wine[i]
        # _OXO
        memo[i][1] = max(memo[i - 2]) + wine[i]
        # _XOO
        memo[i][0] = max(memo[i - 1][1], memo[i - 1][2]) + wine[i]
    #

    # memo = [0] * N
    # memo[0] = wine[0]
    # memo[1] = wine[0] + wine[1]
    # memo[2] = max(wine[0] + wine[1], wine[0]+wine[2], wine[1]+wine[2])
    # for i in range(3, N):
    #     memo[i] = max(memo[i-1], memo[i-2]+wine[i], memo[i-3]+wine[i-1]+wine[i])
    #
    # result = max(memo)
    #
    # print(result)