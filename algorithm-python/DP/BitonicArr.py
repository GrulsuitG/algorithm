# 백준 11054
import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))


def ascArr(n):
    asc = [arr[0]]

    for i in range(1, n + 1):
        target = arr[i]

        if asc[-1] < target:
            asc.append(target)
        else:
            s = 0
            l = len(asc)

            while s < l:
                m = (s + l) // 2
                if asc[m] < target:
                    s = m + 1
                else:
                    l = m
            asc[l] = target
    # print(asc)
    return len(asc)


def descArr(n):
    desc = [arr[N-1]]

    for i in range(N-2, n-1, -1):
        target = arr[i]

        if desc[-1] < target:
            desc.append(target)
        else:
            s = 0
            l = len(desc)

            while s < l:
                m = (s + l) // 2
                if desc[m] < target:
                    s = m + 1
                else:
                    l = m
            desc[l] = target
    # print(desc)
    return len(desc)


result = 0
for i in range(0, N):
    result = max(ascArr(i) + descArr(i) - 1, result)
    # print()

print(result)

