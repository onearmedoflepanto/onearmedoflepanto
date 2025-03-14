from collections import deque

directions = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]


def bfs(n, start, target):
    dq = deque()
    sx, sy, sd = start
    dq.append((sx, sy, sd, 0))
    visited = {}

    while dq:
        x, y, d, cost = dq.popleft()
        if (x, y) == target:
            return cost, (x, y, d)
        # 이미 더 적은 비용으로 도달한 적이 있으면 건너뛰기
        if (x, y, d) in visited and visited[(x, y, d)] <= cost:
            continue
        visited[(x, y, d)] = cost

        # 직진: 현재 방향 그대로 이동, 비용 변화 없음
        dx, dy = directions[d]
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n:
            if (nx, ny, d) not in visited or visited[(nx, ny, d)] > cost:
                dq.appendleft((nx, ny, d, cost))

        # 우회전: 시계방향 90도 회전 후 이동, 비용 +1
        nd = (d + 1) % 4  # 우회전한 후의 방향
        dx, dy = directions[nd]
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n:
            new_cost = cost + 1
            if (nx, ny, nd) not in visited or visited[(nx, ny, nd)] > new_cost:
                dq.append((nx, ny, nd, new_cost))
    # 항상 도달 가능하다고 가정
    return float('inf'), None


def get_queens(n, board):
    queens = []
    num = 1
    while True:
        found = False
        for i in range(n):
            for j in range(n):
                if board[i][j] == num:
                    queens.append((i, j))
                    found = True
        if not found:
            break
        num += 1
    return queens


t = int(input())

for tc in range(1, t+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    queens = get_queens(n, board)

    current_state = (0, 0, 0)
    total_cost = 0

    for queen in queens:
        cost, new_state = bfs(n, current_state, queen)
        total_cost += cost
        current_state = new_state
    print(f"# {tc} {total_cost}")
