def solution(rows, columns, queries):
    answer = [0] * len(queries)
    mat = [[0 for j in range(columns)] for i in range(rows)]
    idx = 1
    for i in range(rows):
        for j in range(columns):
            mat[i][j] = idx
            idx += 1
    for row in mat:
        print(row)
    for idx, query in enumerate(queries):
        mat, answer[idx] = rotate(mat, query)

    return answer


def rotate(mat, query):
    x1, y1, x2, y2 = query
    up = mat[x1 - 1][y1 - 1:y2-1]
    down = mat[x2 - 1][y1:y2]
    left = [mat[row][y1-1] for row in range(x1,x2)]
    right = [mat[row][y2 - 1] for row in range(x1-1,x2-1)]

    answer = min(min(up, down, left, right))
    mat[x1 - 1][y1:y2] = up
    mat[x2 - 1][y1-1:y2-1] = down
    for row in range(x1,x2):
        mat[row][y2-1] = right[row-x1]
    for row in range(x1-1,x2-1):
        mat[row][y1-1] = left[row-x1+1]

    return mat, answer

print(solution(6,7,[[]]))