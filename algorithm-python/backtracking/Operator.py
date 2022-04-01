import math

min_res = math.inf
max_res = -math.inf


def calculator(time, temp_result):
    global min_res, max_res
    if time == num:
        min_res = min(min_res, temp_result)
        max_res = max(max_res, temp_result)
        return
    elif time == 1:
        first = numbers[0]
        second = numbers[1]
    else:
        first = temp_result
        second = numbers[time]

    for op in range(0, 4):
        if operator[op] != 0:
            if op == 0:
                temp_result = first + second
            elif op == 1:
                temp_result = first - second
            elif op == 2:
                temp_result = first * second
            elif op == 3:
                temp_result = int(first / second)
            operator[op] -= 1

            calculator(time + 1, temp_result)
            operator[op] += 1


num = int(input())

numbers = list(map(int, input().split()))

operator = list(map(int, input().split()))

calculator(1, 0)

print(max_res)
print(min_res)
