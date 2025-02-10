from collections import deque

def bfs_path(start, target, initial_direction, is_valid):
    """
    주어진 시작 상태에서 목표 상태까지 도달하는 최소 우회전 횟수,
    최종 진행 방향, 그리고 경로(상태의 리스트)를 반환하는 0–1 BFS 함수입니다.
    
    매개변수:
      - start: (x, y) 형태의 시작 좌표
      - target: (x, y) 형태의 목표 좌표
      - initial_direction: 시작 시 진행 방향 (예: 0: 오른쪽, 1: 아래, 2: 왼쪽, 3: 위)
      - is_valid: (x, y) 좌표가 이동 가능한(예, 체스판의 변 위에 있는)지를 판별하는 함수
    
    반환값:
      - cost: 목표까지 도달하는 데 필요한 최소 우회전 횟수
      - final_direction: 목표에 도착했을 때의 진행 방향
      - path: 시작 상태부터 목표 상태까지 도달한 상태들의 리스트
              각 상태는 (x, y, direction) 형태입니다.
    """
    # 방향: 0=오른쪽, 1=아래, 2=왼쪽, 3=위
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    dq = deque()
    start_state = (start[0], start[1], initial_direction)
    dq.append(start_state)
    
    # 각 상태까지의 누적 비용 저장
    dist = {start_state: 0}
    # 경로 복원을 위한 사전: 각 상태가 (이전 상태, 이동 종류) 형태로 저장됨.
    # 시작 상태는 이전 정보가 없으므로 None을 저장합니다.
    prev = {start_state: None}
    
    while dq:
        x, y, d = dq.popleft()
        current_cost = dist[(x, y, d)]
        
        # 목표 좌표에 도달하면 (방향은 상관없이 좌표만 비교)
        if (x, y) == target:
            # 경로 복원: 시작 상태부터 현재 상태까지의 경로를 만들어냅니다.
            path = []
            cur = (x, y, d)
            while cur is not None:
                path.append(cur)
                # prev[cur]가 None이면 복원 종료, 아니면 이전 상태를 가져옵니다.
                cur = prev[cur][0] if prev[cur] is not None else None
            path.reverse()
            return current_cost, d, path
        
        # 1. 직진 (비용 0): 현재 방향 그대로 한 칸 이동
        nx, ny = x + dx[d], y + dy[d]
        nd = d  # 방향 변화 없음
        if is_valid(nx, ny):
            next_state = (nx, ny, nd)
            if next_state not in dist or dist[next_state] > current_cost:
                dist[next_state] = current_cost
                prev[next_state] = ((x, y, d), 'straight')
                dq.appendleft(next_state)  # 비용 0이므로 앞쪽에 추가
        
        # 2. 우회전 (비용 1): 현재 방향에서 90도 우회전 후 한 칸 이동
        nd = (d + 1) % 4  # 우회전한 후의 방향
        nx, ny = x + dx[nd], y + dy[nd]
        if is_valid(nx, ny):
            next_state = (nx, ny, nd)
            if next_state not in dist or dist[next_state] > current_cost + 1:
                dist[next_state] = current_cost + 1
                prev[next_state] = ((x, y, d), 'right_turn')
                dq.append(next_state)  # 비용 1이므로 뒤쪽에 추가
    
    # 목표에 도달할 수 없는 경우 (문제 조건상 발생하지 않을 것으로 예상)
    return float('inf'), None, []


def process_game(game_moves, is_valid, initial_direction=0):
    """
    여러 폰의 이동(게임 전체)을 처리하는 함수입니다.
    
    매개변수:
      - game_moves: 각 폰의 이동을 나타내는 리스트.
                    각 요소는 ((start_x, start_y), (target_x, target_y)) 형태의 튜플입니다.
      - is_valid: 좌표 (x, y)가 이동 가능한지를 판단하는 함수.
                  예를 들어, 체스판의 변(테두리)에 있는지 여부를 확인.
      - initial_direction: 첫 번째 폰의 시작 진행 방향 (기본값은 0, 즉 오른쪽)
    
    반환값:
      - total_cost: 모든 폰의 이동에서의 누적 최소 우회전 횟수
      - results: 각 이동에 대한 결과 리스트.
                 각 결과는 딕셔너리 형태로, 'start', 'target', 'cost', 'final_direction', 'path' 항목을 가집니다.
                 path는 해당 이동의 경로(상태들의 리스트)를 나타냅니다.
    """
    total_cost = 0
    results = []
    current_direction = initial_direction
    
    for move in game_moves:
        start, target = move
        cost, final_direction, path = bfs_path(start, target, current_direction, is_valid)
        results.append({
            'start': start,
            'target': target,
            'cost': cost,
            'final_direction': final_direction,
            'path': path
        })
        total_cost += cost
        # 다음 폰의 시작 방향은 이번 이동의 최종 방향으로 설정
        current_direction = final_direction if final_direction is not None else current_direction
    
    return total_cost, results


# 예시: 체스판 테두리(예를 들어 8x8 체스판)의 이동 유효성 검사 함수
def is_valid_on_border(x, y, board_size=8):
    """
    좌표 (x, y)가 board_size x board_size 체스판의 '변(테두리)' 위에 있으면 True를 반환합니다.
    """
    if 0 <= x < board_size and 0 <= y < board_size:
        return x == 0 or y == 0 or x == board_size - 1 or y == board_size - 1
    return False


# ---------------------------------------------
# 사용 예시
# ---------------------------------------------
if __name__ == "__main__":
    # 게임에서 각 폰의 이동 (예시)
    # 예를 들어, 첫 번째 폰은 (0, 0)에서 시작하여 (7, 0)으로, 두 번째 폰은 (7, 0)에서 시작하여 (7, 7)로 이동하는 식이라고 가정.
    game_moves = [
        ((0, 0), (7, 0)),
        ((7, 0), (7, 7)),
        ((7, 7), (0, 7)),
        ((0, 7), (0, 0))
    ]
    
    total_cost, move_results = process_game(game_moves, is_valid_on_border, initial_direction=0)
    
    print("전체 우회전 비용:", total_cost)
    for result in move_results:
        print("시작:", result['start'], "→ 목표:", result['target'])
        print("  우회전 비용:", result['cost'])
        print("  최종 방향:", result['final_direction'])
        print("  경로:", result['path'])


def is_same(a,b):
    if len(a) != len(b):
        return False
    for i in range(len(a)):
            if a[i] != b[i]:
                return False