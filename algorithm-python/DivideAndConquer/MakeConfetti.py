# 백준 2630번
import sys


def divide(size, board):
    if size == 1:
        if board[0][0] == '0':
            return 1, 0
        else:
            return 0, 1
    else:
        next_size = size // 2
        white = blue = 0
        for i in range(2):
            for j in range(2):
                temp1, temp2 = divide(next_size, list(
                    row[next_size * i:next_size * (i + 1)] for row in board[next_size * j:next_size * (j + 1)]))
                white += temp1
                blue += temp2

        if white == 4 and blue == 0:
            white, blue = 1, 0

        if blue == 4 and white == 0:
            white, blue = 0, 1
        return white, blue


N = int(sys.stdin.readline())
board = [sys.stdin.readline().split() for _ in range(N)]

w, b = divide(N, board)
print(w)
print(b)