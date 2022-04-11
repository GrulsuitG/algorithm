# 백준 9251번
import sys

strA = sys.stdin.readline()
strB = sys.stdin.readline()

lenA = len(strA)
lenB = len(strB)

dp = [[0] * lenB for _ in range(lenA)]
cnt = 1
for i in range(1, lenA):
    a = strA[i-1]
    for j in range(1, lenB):
        b = strB[j-1]
        if a == b:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[lenA-1][lenB-1])