# 백준 5430번
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    func = sys.stdin.readline()
    N = int(sys.stdin.readline())

    arr = sys.stdin.readline().rstrip()[1:-1].split(',')
    if N == 0:
        arr = []
    front = 0
    back = 0
    direction = True
    func.replace('RR', '')
    for f in func:
        if f == 'R':
            direction = not direction
        elif f == 'D':
            if direction:
                front += 1
            else:
                back += 1
    if front + back <= N:
        arr = arr[front:N - back]
        if not direction:
            arr = arr[::-1]
        sys.stdout.write('[' + ','.join(arr) + ']\n')
    else:
        sys.stdout.write('error\n')

