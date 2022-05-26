def solution(n, edge):
    edges = {i: [] for i in range(1, n + 1)}
    for e in edge:
        edges[e[0]].append(e[1])
        edges[e[1]].append(e[0])
    queue = [1]
    visit = [0] * (n + 1)
    distance = [0] * (n + 1)
    while len(queue):
        cur = queue.pop(0)
        visit[cur] = 1
        for vertex in edges[cur]:
            if not visit[vertex]:
                queue.append(vertex)
                distance[vertex] = distance[cur] + 1
                visit[vertex] = 1

    return distance.count(max(distance))

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))