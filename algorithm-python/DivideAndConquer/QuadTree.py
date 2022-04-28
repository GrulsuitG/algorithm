# 백준 1992번
import sys

def quad_tree(N, board):
    if N == 1:
        if board[0][0] == '1':
            return '1'
        else:
            return '0'

    result = ''
    next_N = N // 2
    for i in range(2):
        for j in range(2):
            result += quad_tree(next_N, [row[next_N * j: next_N * (j+1)] for row in board[next_N * i : next_N * (i+1)]])

    if result == '1111':
        result = '1'
    elif result == '0000':
        result = '0'
    else:
        result = '(' + result + ')'

    return result


N = int(sys.stdin.readline())
board = [list(sys.stdin.readline().strip()) for _ in range(N)]

print(quad_tree(N, board))