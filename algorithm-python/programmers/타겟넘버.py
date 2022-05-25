def solution(numbers, target):
    cur = [numbers[0], -numbers[0]]
    for i in range(1, len(numbers)):
        temp = []
        for item in cur:
            temp.append(item + numbers[i])
            temp.append(item - numbers[i])
        cur = temp
    return cur.count(target)


def best(numbers, target):
    if not numbers and target == 0:
        return 1
    elif not numbers:
        return 0
    else:
        return best(numbers[1:], target-numbers[0]) + best(numbers[1:], target+numbers[0])


