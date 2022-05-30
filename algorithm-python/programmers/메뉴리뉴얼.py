from collections import defaultdict, Counter
from itertools import combinations


def solution(orders, course):
    answer = []
    temp = defaultdict(set)
    for idx, order in enumerate(orders):
        for menu in order:
            temp[menu].add(idx)

    trx = {}
    for key, item in temp.items():
        if len(item) > 1:
            trx[key] = item
    prev = 1
    for n in course:
        cnt = 2
        arr = []
        if prev < 1:
            break
        for items in combinations(trx.keys(), n):
            inter = trx[items[0]].intersection(trx[items[1]])
            for i in range(2, n):
                inter = inter.intersection(trx[items[i]])

            if len(inter) > cnt:
                cnt = len(inter)
                arr = [''.join(sorted(items))]
            elif len(inter) == cnt:
                arr.append(''.join(sorted(items)))
        prev = len(arr)
        if cnt > 1:
            answer.extend(arr)

    answer.sort()
    return answer


def best(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += combinations(sorted(order), course_size)

        most_ordered = Counter(order_combinations).most_common()
        result += [k for k, v in most_ordered if v > 1 and v == most_ordered[0][1]]

    return [''.join(v) for v in sorted(result)]


best(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])