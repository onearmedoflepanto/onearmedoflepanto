tc = int(input())

for t in range(1, tc + 1):
    n = int(input())
    field = [list(map(int, input().split())) for _ in range(n)]

    numbers = {}
    points = [(0, 0)]

    for i in range(n):
        for j in range(n):
            if field[i][j] != 0:
                num = field[i][j]
                numbers[num] = (i, j)
                points.append((i, j))

    dist_matrix = {
        (p1, p2): (lambda a, b: abs(a[0] - b[0]) + abs(a[1] - b[1]))(p1, p2)
        for p1 in points for p2 in points
    }

    num_cnt = len(numbers)
    dp = [[float('inf')] * (num_cnt+1) for _ in range(1 << num_cnt + 1)]
    dp[1][0] = 0
    point_index = {point: i for i, point in enumerate(points)}

    for mask in range(1 << (num_cnt + 1)):
        for i in range(num_cnt + 1):
            if dp[mask][i] == float('inf'):
                continue

            for j in range(num_cnt + 1):
                if (mask & (1 << j)) == 0:
                    next_mask = mask | (1 << j)

                    current_num = field[points[i][0]][points[i][1]]
                    next_num = field[points[j][0]][points[j][1]]

                    if next_num < 0:
                        pos_num = -next_num
                        if pos_num not in numbers or (mask & (1 << point_index[numbers[pos_num]])) == 0:
                            continue

                    dp[next_mask][j] = min(
                        dp[next_mask][j], dp[mask][i] + dist_matrix[(points[i], points[j])])

    full_mask = (1 << (num_cnt + 1)) - 1
    res = min(dp[full_mask])
    print(f"#{t} {res}")
