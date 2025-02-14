def infrared_camera(field, x, y, k):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        for dist in range(1, k+1):
            nx, ny = x + dx * dist, y + dy * dist
            
            # 격자 범위를 벗어나면 해당 방향 진행 중단
            if not (0 <= nx < 10 and 0 <= ny < 10):
                break
            
            # 다른 카메라(1, 2, 3) 또는 벽(4)이 있으면 진행 중단
            if field[nx][ny] in [1, 2, 3, 4]:
                break
            
            # 빈 칸에 정수 9를 표시
            field[nx][ny] = 9
    return field

t_input = int(input())

for t in range(1, t_input+1):
    n = int(input())
    field = [list(map(int, input().strip())) for _ in range(10)]
    
    # 각 카메라의 위치를 찾습니다.
    rcamera_positions = [(i, j) for i in range(10) for j in range(10) if field[i][j] == 1]
    gcamera_positions = [(i, j) for i in range(10) for j in range(10) if field[i][j] == 2]
    bcamera_positions = [(i, j) for i in range(10) for j in range(10) if field[i][j] == 3]
    
    # 카메라 종류별로 적외선 효과 적용
    for x, y in rcamera_positions:
        infrared_camera(field, x, y, 1)
    for x, y in gcamera_positions:
        infrared_camera(field, x, y, 2)
    for x, y in bcamera_positions:
        infrared_camera(field, x, y, 3)
    
    zero_position = [(i,j) for i in range(10) for j in range(10) if field[i][j] == 0]

    print(f"#{t} {len(zero_position)}")