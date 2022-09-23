from pprint import pprint


def solution(board, skills):
    answer = 0
    n = len(board)
    m = len(board[0])

    accSum = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for skill in skills:
        t, r1, c1, r2, c2, degree = skill
        t = 1 if t == 2 else -1
        accSum[r1][c1] += degree * t
        accSum[r1][c2 + 1] -= degree * t
        accSum[r2 + 1][c1] -= degree * t
        accSum[r2 + 1][c2 + 1] = degree * t
    for i in range(n):
        for j in range(1, m):
            accSum[i][j] += accSum[i][j - 1]
    for i in range(1, n):
        for j in range(m):
            accSum[i][j] += accSum[i - 1][j]

    for i in range(n):
        for j in range(m):
            board[i][j] += accSum[i][j]
            if board[i][j] + accSum[i][j] > 0:
                answer += 1

    for row in board:
        print(row)
    return answer

solution([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]], [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]])