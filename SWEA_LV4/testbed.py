import heapq

tc = int(input())

for t in range(1, tc + 1):
    n = int(input())
    field = [list(map(int, input().split())) for _ in range(n)]

    hq = []
    heapq.heappush(hq, (field[0][0], 0, 0))
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    distances = [[float('inf')] * n for _ in range(n)]
    distances[0][0] = field[0][0]

    while hq:
        cost, x, y = heapq.heappop(hq)

        if cost > distances[x][y]:
            continue

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                new_cost = cost + field[nx][ny]
                if new_cost < distances[nx][ny]:
                    distances[nx][ny] = new_cost
                    heapq.heappush(hq, (new_cost, x, y))

    print(f"{t} {distances[n-1][n-1]}")
