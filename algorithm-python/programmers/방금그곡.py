def solution(m, musicinfos):
    answer = "(None)"
    playTime = 0
    m = change(m)
    for musicinfo in musicinfos:
        start, end, title, info = musicinfo.split(',')
        startH, startM = start.split(':')
        endH, endM = end.split(':')

        time = int(endH) * 60 + int(endM) - int(startH) * 60 - int(startM) + 1
        info = change(info) * 2
        if time < len(info):
            info = info[:time]
        while len(info) < time:
            info += info
        if m in info:
            if playTime < time:
                answer = title
                playTime = time

    return answer


def change(melody):
    return melody.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')


solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:59,14:01,WORLD,ABCDEF"])
