# 백준 11444번
import sys

def multiple(m1, m2):
    temp = [[0, 0], [0, 0]]
    temp[0][0] = (m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0]) % R
    temp[0][1] = (m1[0][0] * m2[0][1] + m1[0][1] * m2[1][1]) % R
    temp[1][0] = (m1[1][0] * m2[0][0] + m1[1][1] * m2[1][0]) % R
    temp[1][1] = (m1[1][0] * m2[0][1] + m1[1][1] * m2[1][1]) % R
    return temp

def power(n):
    if n == 1:
        return mat
    else:
        if n % 2 == 0:
            temp = power(n // 2)
            return multiple(temp, temp)
        else:
            temp = power(n - 1)
            return multiple(temp, mat)

N = int(sys.stdin.readline())
R = 1_000_000_007

mat = [[1, 1], [1, 0]]

res = power(N)
print(res[0][1] % R)
