import copy

def solution(key, lock):
    answer = True
    M = len(key)
    N = len(lock)
    size = N * 3

    board = [[0] * size for _ in range(size)]

    for i in range(N):
        for j in range(N):
            board[i + N][j + N] = lock[i][j]

    print('init')
    for row in board:
        print(row)
    print()

    for _ in range(4):
        for i in range(size - N):
            for j in range(size - N):
                conflict, temp = key_in_lock(board, key, M, i, j)

                if conflict:
                    print(i, j, 'conflict')
                    continue

                if check(temp, N):
                    print(i, j, 'check')
                    return True

                print()

        key = [[row[i] for row in key[::-1]] for i in range(M)]

    return False


def check(board, N):
    for x in range(N):
        for y in range(N):
            if board[x + N][y + N] != 1:
                return False
    return True


def key_in_lock(board, key, M, x, y):
    temp = copy.deepcopy(board)
    for i in range(M):
        for j in range(M):
            if temp[x + i][y + j] ^ key[i][j]:
                temp[x + i][y + j] = 1
            elif temp[x + i][y + j] == key[i][j] == 1:
                return True, temp

    return False, temp


solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])