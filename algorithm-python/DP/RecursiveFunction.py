# 백준 9184번
import sys

memo = [[[-1]*21 for _ in range(21)] for _ in range(21)]


def w(a, b, c):
    global memo

    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    if memo[a][b][c] != -1:
        return memo[a][b][c]

    if a < b < c:
        result = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)

    else:
        result = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)

    memo[a][b][c] = result
    return result


while True:
    a, b, c = map(int, sys.stdin.readline().split())

    if a == b == c == -1:
        break
    print("w(%d, %d, %d) = %d" % (a, b, c, w(a, b, c)))