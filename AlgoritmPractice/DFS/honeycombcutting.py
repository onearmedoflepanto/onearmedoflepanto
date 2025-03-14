import sys
sys.stdin = open("2.in", 'r')

odd_directions = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
    (1, -1),
    (1, 1)
]

even_directions = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, -1),
    (-1, 1)
]


def dfs(r, c, count, cost, prev):
    global answer, honeycomb, N, M
    if count == 4:
        answer = max(answer, cost)
        return

    directions = even_directions if c % 2 == 0 else odd_directions

    temp = honeycomb[r][c]
    honeycomb[r][c] = -1

    for dx, dy in directions:
        nr, nc = r + dx, c + dy
        if 0 <= nr < N and 0 <= nc < M and honeycomb[nr][nc] != -1:
            dfs(nr, nc, count + 1, cost + temp, prev=(r, c))

    if prev is not None:
        pr, pc = prev
        prev_directions = even_directions if pc % 2 == 0 else odd_directions
        for dx, dy in prev_directions:
            nr, nc = pr + dx, pc + dy
            if 0 <= nr < N and 0 <= nc < M and honeycomb[nr][nc] != -1:
                dfs(nr, nc, count + 1, cost + temp, prev=(r, c))

    honeycomb[r][c] = temp


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    honeycomb = [list(map(int, input().split())) for _ in range(N)]
    answer = float('-inf')

    for r in range(N):
        for c in range(M):
            dfs(r, c, 0, 0, prev=None)

    print(f"#{t} {answer}")
