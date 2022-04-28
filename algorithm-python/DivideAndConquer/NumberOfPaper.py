# 백준 1780번
import sys

def sol(N, board):
    if N == 1:
        if board[0][0] == '-1':
            return [1, 0, 0]
        elif board[0][0] == '0':
            return [0, 1, 0]
        elif board[0][0] == '1':
            return [0, 0, 1]

    n = N // 3
    arr = [0, 0, 0]
    for i in range(3):
        for j in range(3):
            temp = sol(n, [row[n * j: n * (j + 1)] for row in board[n * i: n * (i + 1)]])
            arr[0] += temp[0]
            arr[1] += temp[1]
            arr[2] += temp[2]

    if arr == [9, 0, 0]:
        arr = [1, 0, 0]
    elif arr == [0, 9, 0]:
        arr = [0, 1, 0]
    elif arr == [0, 0, 9]:
        arr = [0, 0, 1]

    return arr


N = int(sys.stdin.readline())
board = [sys.stdin.readline().split() for _ in range(N)]

result = sol(N, board)
print('\n'.join(map(str, result)))
