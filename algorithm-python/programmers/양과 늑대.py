from collections import defaultdict

answer = -1

def solution(info, edges):
    node = defaultdict(list)
    for parent, child in edges:
        node[parent].append(child)

    def dfs(curidx, lamb, wolf, queue):
        global answer
        
        if info[curidx] == 0:
            lamb += 1
            answer = max(answer, lamb)
        else:
            wolf += 1

        if wolf >= lamb:
            return

        queue.extend(node[curidx])

        for nextidx in queue:
            next_que = queue.copy()
            next_que.remove(nextidx)
            dfs(nextidx, lamb, wolf, next_que)

    dfs(0, 0, 0, [])
    return answer


a = solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]])
print(a)