def get_area(co1, co2):
    x1, y1 = co1
    x2, y2 = co2
    return (x2 - x1 + 1) * (y2 - y1 + 1)

t_input = int(input())

for _ in range(t_input):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    
    overall_max_area = 0
    count_max_area = 0

    # k가 board에 나타날 수 있는 숫자라 가정 (예: 0 ~ 19)
    for k in range(20):
        # 해당 숫자 k의 좌표 모으기
        co = [(i, j) for i in range(n) for j in range(n) if board[i][j] == k]
        
        # 유효한 (좌상단, 우하단) 쌍만 고려
        valid_pairs = [(co1, co2) for co1 in co for co2 in co 
                       if co1[0] <= co2[0] and co1[1] <= co2[1]]
        
        if not valid_pairs:
            continue

        # k에 대해 최대 면적과 그 개수를 구함
        max_area = 0
        count = 0
        
        for co1, co2 in valid_pairs:
            area_candidate = get_area(co1, co2)
            if area_candidate > max_area:
                max_area = area_candidate
                count = 1
            elif area_candidate == max_area:
                count += 1
        
        # 전체 최대 면적과 비교 및 업데이트
        if max_area > overall_max_area:
            overall_max_area = max_area
            count_max_area = count
        elif max_area == overall_max_area:
            count_max_area += count

    print(count_max_area)