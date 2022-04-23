# 백준 16139번
import bisect
import sys

S = sys.stdin.readline()
q = int(sys.stdin.readline())
alphaNum = [[] for _ in range(26)]

for i in range(len(S) - 1):
    idx = ord(S[i]) - 97
    alphaNum[idx].append(i)

for _ in range(q):
    alpha, l, r = sys.stdin.readline().split()
    l = int(l)
    r = int(r)
    idx = ord(alpha) - 97

    s = bisect.bisect_left(alphaNum[idx], l)
    e = bisect.bisect_right(alphaNum[idx], r)

    sys.stdout.write(str(e - s) + '\n')