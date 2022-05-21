def solution(lines):
    answer = 1
    timetonum(lines)
    for i in range(len(lines)):
        cnt = 1
        for j in range(i+1, len(lines)):
            if lines[i][1] + 1 > lines[j][0]:
                cnt += 1
        answer = max(answer, cnt)
    return answer


def timetonum(lines):
    for idx, times in enumerate(lines):
        times = times.split()
        s = list(map(float, times[1].split(':')))
        t = float(times[2][:-1])
        end = s[0] * 3600 + s[1] * 60 + s[2]
        lines[idx] = [end - t + 0.001, end]


solution(["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"])