from collections import deque


class UnionFind


def cruskal(board):
    """
    모든 물체를 잇는 최소 직선들을 구함
    단 직선의 길이는 1보다 커야 하고
    직선끼리 교차하면 안됨.
    """

    objects = get_objects(board)
    for i in range(len(objects)):
        for j in range(i+1, len(objects)):
            lines.extend(get_lines(objects[i], objects[j]))


def get_objects(board):
    """
    보드에서 1로 이루어진 물체들을 구함
    """
    n, m = len(board), len(board[0])
    res = []
    visited = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if board[i][j] == 1 and visited[i][j] == 0:
                visited[i][j] = 1
                q = deque()
                q.append((i, j))
                minr, minc, maxr, maxc = i, j, i, j
                while q:
                    r, c = q.popleft()
                    maxr = max(r, maxr)
                    maxc = max(c, maxc)
                    minr = min(r, minr)
                    minc = min(c, minc)
                    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < m:
                            if board[nr][nc] == 1 and visited[nr][nc] == 0:
                                visited[nr][nc] = 1
                                q.append((nr, nc))
                res.append(((minr, minc), (maxr, maxc)))

    return res


def get_lines(obj1, obj2):
    """
    두 물체 사이를 잇는 직선을 전부 구함.
    단, 길이가 1인 직선은 제외.
    """
    lines = []
    start, end = obj1
    (obj1_x1, obj1_y1) = start
    (obj1_x2, obj1_y2) = end
    start, end = obj2
    (obj2_x1, obj2_y1) = start
    (obj2_x2, obj2_y2) = end

    # 수평선 찾기
    if obj1_x2 < obj2_x1 - 1 or obj2_x2 < obj1_x1 - 1:
        common_y = set(range(obj1_y1, obj1_y2 + 1)
                       ) & set(range(obj2_y1, obj2_y2 + 1))
        if common_y:
            for y in common_y:
                lines.append(((obj1_x2, y), (obj2_x1, y)))

    # 수직선 찾기
    if obj1_y2 < obj2_y1 - 1 or obj2_y2 < obj1_y1 - 1:
        common_x = set(range(obj1_x1, obj1_x2 + 1)
                       ) & set(range(obj2_x1, obj2_x2 + 1))
        if common_x:
            for x in common_x:
                lines.append(((x, obj1_y2), (x, obj2_y1)))

    return lines


# 입력부
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
objects = get_objects(board)
lines = []

# mst = cruskal(board)
