def gravity(field, direction):
    n = len(field)
    new_field = [[0] * n for _ in range(n)]

    if direction == 'vertical':
        for col in range(n):
            count = 0
            for row in range(n):
                if field[row][col] == 1:
                    count += 1
                else:
                    break
            if count != 1:
                for row in range(n):
                    new_field[row][col] = field[row][col]
                continue

            col_list = [field[row][col] for row in range(n)]
            fallen = row_fall(col_list)
            for row in range(n):
                new_field[row][col] = fallen[row]
        return new_field

    elif direction == 'horizontal':
        for row in range(n):
            count = 0
            for col in range(n):
                if field[row][col] == 1:
                    count += 1
                else:
                    break
            if count != 1:
                new_field[row] = field[row][:]
                continue

            new_field[row] = row_fall(field[row])
        return new_field


def row_fall(row):
    n = len(row)
    work = row[:]

    cluster_weight = 0
    while cluster_weight < n and work[cluster_weight] == 1:
        cluster_weight += 1

    for i in range(cluster_weight):
        work[i] = 0

    falling_pos = 0
    collision_force = 1.0

    if sum(work) == 0:
        falling_pos = n - cluster_weight
    else:
        while True:
            gap = 0
            pos = falling_pos + cluster_weight
            while pos < n and work[pos] == 0:
                gap += 1
                pos += 1

            collision_force *= (1.9 ** gap)

            if pos >= n:
                falling_pos += gap
                if falling_pos + cluster_weight > n:
                    falling_pos = n - cluster_weight
                break

            stat_weight = 0
            start_stat = pos
            while pos < n and work[pos] == 1:
                stat_weight += 1
                pos += 1

            if collision_force > stat_weight:
                cluster_weight += stat_weight
                collision_force += stat_weight
                for i in range(start_stat, start_stat + stat_weight):
                    work[i] = 0
                falling_pos += gap
                if falling_pos + cluster_weight > n:
                    falling_pos = n - cluster_weight
                    break
            else:
                falling_pos += gap
                break

    new_row = work[:]
    for i in range(falling_pos, falling_pos + cluster_weight):
        if i < n:
            new_row[i] = 1
    return new_row


tc = int(input())
for t in range(1, tc+1):
    n = int(input())
    field = [list(map(int, input().split())) for _ in range(n)]

    field = gravity(field, 'vertical')

    # print()
    # for row in field:
    #     print(*row)

    field = gravity(field, 'horizontal')

    # print()
    # for row in field:
    #     print(*row)

    row_count = field[-1].count(1)
    column_count = sum(1 for i in range(n) if field[i][-1] == 1)

    print(f"#{t} {row_count} {column_count}")
