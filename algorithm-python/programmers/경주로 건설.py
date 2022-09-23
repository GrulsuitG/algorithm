from pprint import pprint
import heapq

def solution(board):
    answer = 0
    n = len(board)
    prices = [[[987654321 for i in range(4)] for j in range(n)] for k in range(n)]
    #남동북서
    direction = [(1,0), (0,1), (-1,0), (0, -1)]
    heap = []
    for i in range(2):
        heapq.heappush(heap, (0, 0, 0, i))

    while heap:
        cost, x, y, face = heapq.heappop(heap)

        for i in range(4):
            nx, ny = x + direction[i][0], y + direction[i][1]

            # 범위가 넘어가는 경우
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            # 장애물
            if board[nx][ny] == 1:
                continue

            # 역 방향
            elif abs(i - face) == 2:
                continue

            #같은 방향
            if face == i:
                next_cost = cost + 100

            #커브
            else:
                next_cost = cost + 600

            if prices[nx][ny][i] > next_cost:
                prices[nx][ny][i] = next_cost
                heapq.heappush(heap, (next_cost, nx, ny, i))


    return min(prices[n - 1][n - 1][i] for i in range(4))

a = solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

print(a)