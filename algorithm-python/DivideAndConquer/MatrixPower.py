# 백준 10830번
import sys


def multiple(m1, m2):
    temp = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            try:
                temp[i][j] += (m1[i][0] * m2[0][j])
                temp[i][j] += (m1[i][1] * m2[1][j])
                temp[i][j] += (m1[i][2] * m2[2][j])
                temp[i][j] += (m1[i][3] * m2[3][j])
                temp[i][j] += (m1[i][4] * m2[4][j])
            except Exception:
                pass
            temp[i][j] %= R
    return temp


R = 1000
N, B = map(int, sys.stdin.readline().split())
mat = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def power(B):
    if B == 1:
        return mat
    else:
        if B % 2 == 0:
            temp = power(B // 2)
            return multiple(temp, temp)
        else:
            temp = power(B-1)
            return multiple(temp, mat)


res = power(B)
for i in range(N):
    for j in range(N):
        res[i][j] %= R

for row in res:
    sys.stdout.write(' '.join(map(str, row)) + '\n')

