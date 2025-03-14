import heapq

directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

t = int(input().strip())


def dijkstra(heap):
    while heap:
        cur_cost, x, y = heapq.heappop(heap)

        if x == n - 1 and y == n - 1:
            return cur_cost

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if field[nx][ny] > field[x][y]:
                    cost = 2 * (field[nx][ny] - field[x][y])
                elif field[nx][ny] == field[x][y]:
                    cost = 1
                else:
                    cost = 0
                new_cost = cur_cost + cost
                if new_cost < distance[nx][ny]:
                    distance[nx][ny] = new_cost
                    heapq.heappush(heap, (new_cost, nx, ny))

        if (x, y) in tunnels:
            for (tx, ty, k) in tunnels[(x, y)]:
                new_cost = cur_cost + k
                if new_cost < distance[tx][ty]:
                    distance[tx][ty] = new_cost
                    heapq.heappush(heap, (new_cost, tx, ty))


for tc in range(1, t + 1):
    n, m = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(n)]
    tunnels = {}

    for _ in range(m):
        ay, ax, by, bx, k = map(int, input().split())
        ay, ax, by, bx = ay - 1, ax - 1, by - 1, bx - 1

        if (ay, ax) not in tunnels:
            tunnels[(ay, ax)] = []
        if (by, bx) not in tunnels:
            tunnels[(by, bx)] = []

        tunnels[(ay, ax)].append((by, bx, k))
        tunnels[(by, bx)].append((ay, ax, k))

    q = []
    heapq.heappush(q, (0, 0, 0))
    distance = [[float('inf')] * n for _ in range(n)]
    distance[0][0] = 0
    res = dijkstra(q)

    print(f"#{tc} {res}")
