from collections import defaultdict, deque


def solution(n, wires):
    answer = 100
    tree = defaultdict(list)
    for wire in wires:
        tree[wire[0]].append(wire[1])
        tree[wire[1]].append(wire[0])
    for wire in wires:
        cnt = abs(bfs(wire[1], wire[0], wires, n, tree) - bfs(wire[0], wire[1], wires, n, tree))
        answer = min(cnt, answer)
    return answer

def bfs(start, cut, wires, n, tree) :
    count = 0
    visited = [False] * (n + 1)
    q = deque([start])
    visited[start] = True

    while q :
        v = q.popleft()
        for next in tree[v] :
            if next == cut :
                continue
            if visited[next] :
                continue
            count += 1
            q.append(next)
            visited[next] = True

    return count


