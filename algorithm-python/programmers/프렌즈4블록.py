def solution(m, n, board):
    answer = 0
    board = [list(row) for row in board]

    while True:
        rm = []
        for row in range(m - 1):
            for col in range(n - 1):
                if board[row][col] == board[row][col + 1] == board[row + 1][col] == board[row + 1][col + 1] != ' ':
                    rm.append((row, col))

        if not rm:
            break

        else:
            for r, c in rm:
                board[r][c] = ' '
                board[r][c + 1] = ' '
                board[r + 1][c] = ' '
                board[r + 1][c + 1] = ' '

            for row in range(1, m):
                for col in range(n):
                    if board[row][col] == ' ':
                        for i in range(row, 0, -1):
                            board[i][col], board[i - 1][col] = board[i - 1][col], board[i][col]

    for row in board:
        answer += row.count(' ')

    return answer


solution(8, 5, ["HGNHU", "CRSHV", "UKHVL", "MJHQB", "GSHOT", "MQMJJ", "AGJKK", "QULKK"])
