def dfs(r, c, steps):
    global max_steps
    global max_steps_co
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    if max_steps <= steps:
        max_steps = steps
        i, j = max_steps_co
        max_steps_co = (r, c) if field[r][c] < field[i][j] else (i, j)

    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n:
            if field[nr][nc] - field[r][c] == 1:
                dfs(nr, nc, steps + 1)


tc = int(input())

for t in range(1, tc+1):
    n = int(input())
    field = [list(map(int, input().split())) for _ in range(n)]

    max_steps = 0
    tempv = float('inf')
    for i in range(n):
        for j in range(n):
            if field[i][j] < tempv:
                tempv = field[i][j]
                max_steps_co = (i, j)

    for i in range(n):
        for j in range(n):
            dfs(i, j, 0)
    print(max_steps_co)
    print(f"#{t} {field[max_steps_co[0]][max_steps_co[1]]} {max_steps+1}")
