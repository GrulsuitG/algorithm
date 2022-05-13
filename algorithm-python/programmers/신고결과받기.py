def solution(id_list, report, k):
    answer = [0] * len(id_list)
    table = [[0] * len(id_list) for _ in range(len(id_list))]
    id = {}
    for n, i in enumerate(id_list):
        id[i] = n
    for r in report:
        a, b = r.split()
        table[id[b]][id[a]] = 1

    for i in range(len(id_list)):
        if sum(table[i]) >= k:
            for j in range(len(id_list)):
                if table[i][j] == 1:
                    answer[j] += 1
    return answer

def best_solution(id_list, report, k):
    answer = [0] * len(id_list)
    id = {x: 0 for x in id_list}

    for r in set(report):
        id[r.split()[1]] += 1

    for r in set(report):
        if id[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1