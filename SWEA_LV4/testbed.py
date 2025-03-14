def dfs(r, c, string):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    if len(string) == 7:
        res.add(string)
        return

    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n:
            dfs(nr, nc, string + grid[nr][nc])


tc = int(input())
n = 4
for t in range(1, tc + 1):
    grid = [list(input().split()) for _ in range(n)]
    res = set()

    for i in range(n):
        for j in range(n):
            dfs(i, j, grid[i][j])

    print(f"#{t} {len(res)}")
