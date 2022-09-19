from collections import defaultdict


def solution(fees, records):
    answer = []
    accTime = defaultdict(int)
    parking = {}
    for record in records:
        time, number, kind = record.split()
        hour, minute = time.split(":")
        time = int(hour) * 60 + int(minute)

        if kind == "OUT":
            accTime[number] += time - parking[number]
            parking.pop(number)
        else:
            parking[number] = time

    for remains in parking:
        accTime[remains] += 23 * 60 + 59 - parking[remains]

    for number in sorted(accTime.keys()):
        time = accTime[number]
        if time <= fees[0]:
            answer.append(fees[1])
        else:
            time = int((time - fees[0]) / fees[2]) + 1 if (time - fees[0]) % fees[2] != 0 else int((time - fees[0]) / fees[2])
            answer.append(fees[1] + time * fees[3])

    return answer

solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])