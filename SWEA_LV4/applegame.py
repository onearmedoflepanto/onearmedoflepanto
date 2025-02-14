from collections import deque

# 방향: 0=위, 1=오른쪽, 2=아래, 3=왼쪽
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
INF = float('inf')

def bfs(s, t, start_dir, n):
    sx, sy = s
    tx, ty = t

    # (x, y, 방향)별 최소 우회전 비용을 저장 (3차원 배열)
    distance = [[[INF] * 4 for _ in range(n)] for _ in range(n)]
    distance[sx][sy][start_dir] = 0

    q = deque()
    q.append((sx, sy, start_dir))
    
    while q:
        x, y, d = q.popleft()
        cur_cost = distance[x][y][d]
        
        # 1) 직진: 동일 방향, 비용 0 추가
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < n:
            if cur_cost < distance[nx][ny][d]:
                distance[nx][ny][d] = cur_cost
                q.appendleft((nx, ny, d))
        
        # 2) 우회전: 오른쪽으로 회전한 후 전진, 비용 1 추가
        nd = (d + 1) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]
        if 0 <= nx < n and 0 <= ny < n:
            new_cost = cur_cost + 1
            if new_cost < distance[nx][ny][nd]:
                distance[nx][ny][nd] = new_cost
                q.append((nx, ny, nd))
    
    # 목표지점(tx, ty)에서 네 방향 중 최소 우회전 비용과 그 방향 찾기
    best_cost = INF
    best_dir = -1
    for d in range(4):
        if distance[tx][ty][d] < best_cost:
            best_cost = distance[tx][ty][d]
            best_dir = d

    if best_cost == INF:
        return -1, -1
    else:
        return best_cost, best_dir

# 메인 코드
t_input = int(input())
for tc in range(1, t_input + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    
    # 보드에 있는 숫자는 1부터 k까지 각각 한 개씩 있다고 가정
    k_list = []
    # 1번 폰의 좌표 찾기
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                k_list.append((i, j))
    # 이후 2, 3, ... 순으로 추가
    k_val = 2
    while True:
        cur_positions = [(i, j) for i in range(n) for j in range(n) if board[i][j] == k_val]
        if not cur_positions:
            break
        k_list.extend(cur_positions)
        k_val += 1

    # (0, 0)에서 출발하여 폰들을 순서대로 방문하도록 경로 구성
    path = [(0, 0)] + k_list

    total_cost = 0
    direction = 1  # 초기 방향: 오른쪽 (문제 조건에 맞게 1로 설정)
    for i in range(len(path) - 1):
        cost, direction = bfs(path[i], path[i+1], direction, n)
        if cost == -1:
            total_cost = -1
            break
        total_cost += cost

    print(f"{tc} {total_cost}")
