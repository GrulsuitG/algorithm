from collections import defaultdict


def solution(info, query):
    answer = []

    condition = defaultdict(list)
    for item in info:
        item = item.split()
        for lang in [item[0], "-"]:
            for job in [item[1], "-"]:
                for career in [item[2], "-"]:
                    for food in [item[3], "-"]:
                        condition[lang + job + career + food].append(int(item[4]))

    for cond in condition:
        condition[cond].sort()

    for qry in query:
        qry = qry.replace(" and ", "")
        qry = qry.split()

        score = int(qry[1])
        candidate = condition[qry[0]]

        low = 0
        l = len(candidate)
        high = l - 1
        tmp = l
        while low <= high:
            mid = (low + high) // 2

            if score <= candidate[mid]:
                tmp = mid
                high = mid - 1
            else:
                low = mid + 1

        answer.append(l - tmp)

    return answer

solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
         ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])