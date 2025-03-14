import sys
sys.stdin = open('input.txt', 'r')

directions = [(-1, -1), (0, -1), (1, -1), (1, 0),
              (1, 1), (0, 1), (-1, 1), (-1, 0)]


def countmine(r, c, n, field):
    """ r,c 0좌상 1좌 2좌하 3하 4우하 5우 6우상 7상 """
    counter = 0
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n:
            if field[nr][nc] == '*':
                counter += 1
    return counter


def poptile(r, c, n, field, num_mine):
    if field[r][c] == '*':
        return field

    queue = [(r, c)]
    while queue:
        cr, cc = queue.pop()
        if field[cr][cc] != '.':
            continue

        field[cr][cc] = 'O'
        if num_mine[cr][cc] == 0:
            for dr, dc in directions:
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < n and 0 <= nc < n and field[nr][nc] == '.':
                    queue.append((nr, nc))

    return field


tc = int(input())

for t in range(1, tc + 1):
    n = int(input())
    raw_field = [input() for _ in range(n)]

    field = [list(row) for row in raw_field]

    num_mine = [[0] * n for _ in range(n)]
    pos_tiles = [[] for _ in range(10)]

    for r in range(n):
        for c in range(n):
            if field[r][c] == '*':
                num_mine[r][c] = -1
            else:
                num = countmine(r, c, n, field)
                num_mine[r][c] = num
                if num > 0:
                    pos_tiles[num].append((r, c))

    click_counter = 0
    for r in range(n):
        for c in range(n):
            if num_mine[r][c] == 0 and field[r][c] == '.':
                field = poptile(r, c, n, field, num_mine)
                click_counter += 1

    for i in range(1, 10):
        for r, c in pos_tiles[i]:
            if field[r][c] == '.':
                field = poptile(r, c, n, field, num_mine)
                click_counter += 1

    print(f"#{t} {click_counter}")
