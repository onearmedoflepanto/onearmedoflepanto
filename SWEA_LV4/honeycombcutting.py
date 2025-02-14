def get_neighbor_candidates(x, y):
    if x % 2 == 0:
        offsets = [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, -1), (1, 0)]
    else:
        offsets = [(-1, 0), (-1, 1), (0, -1), (0, 1), (1, 0), (1, 1)]
    
    neighbors = []
    for dx, dy in offsets:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            neighbors.append((nx, ny))
    return neighbors

def dfs(group, candidates, start_idx):
    global global_max, honeycomb

    if len(group) == 4:
        group_sum = sum(honeycomb[x][y] for (x, y) in group)
        if global_max < group_sum:
            global_max = group_sum
        return

    for cell in sorted(candidates):
        new_group = group | {cell}
        new_candidates = set(candidates)
        new_candidates.remove(cell)
        for nb in get_neighbor_candidates(cell[0], cell[1]):
            nb_idx = nb[0] * m + nb[1]
            if nb not in new_group and nb_idx > start_idx:
                new_candidates.add(nb)
        dfs(new_group, new_candidates, start_idx)
    return

t_input = int(input())
for t in range(1, t_input + 1):
    n, m = map(int, input().split())
    honeycomb = [list(map(int, input().split())) for _ in range(n)]
    global_max = -float('inf')
    for x in range(n):
        for y in range(m):
            start_idx = x * m + y
            group = {(x, y)}
            candidates = set()
            for nb in get_neighbor_candidates(x, y):
                nb_idx = nb[0] * m + nb[1]
                if nb_idx > start_idx:
                    candidates.add(nb)
            dfs(group, candidates, start_idx)
    print(f"#{t} {global_max}")