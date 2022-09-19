def solution(msg):
    answer = []
    dictNumber = 1
    charDict = {}
    for alphabet in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        charDict[alphabet] = dictNumber
        dictNumber += 1

    idx = 0
    while idx < len(msg):
        char = msg[idx]
        i = 2
        while idx + i < len(msg):
            if msg[idx:idx + i] in charDict:
                char = msg[idx:idx + i]
                i += 1
            else:
                break

        idx += i - 1
        answer.append(charDict[char])
        if idx < len(msg):
            charDict[msg[idx + i - 1]] = dictNumber
            dictNumber += 1
    return answer

solution("KAKAO")
