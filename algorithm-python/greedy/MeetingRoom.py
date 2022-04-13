#백준 1931번
import sys

N = int(sys.stdin.readline())

meeting = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
meeting.sort(key=lambda time: (time[1], time[0]))

result = 0
finish = -1
for i in range(N):
    if finish <= meeting[i][0]:
        result += 1
        finish = meeting[i][1]

print(result)

