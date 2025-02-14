from collections import deque

def bfs(startx,starty):
    visited[startx][starty] = True

    while queue:
        x,y= queue.popleft()

        if x== n-1 and y==m-1:
            return distance[x][y]
        
        for dx, dy in directions:
            nx = x+dx
            ny = y+dy

            if 0<= nx < n and 0<= ny < m:
                if field[nx][ny] == 0 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    distance[nx][ny] = distance[x][y] +1
                    queue.append((nx, ny))

    return -1

n, m = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
start = (0,0)
visited[0][0] = True
queue = deque([start])
directions = [(1,0),(-1,0),(0,1),(0,-1)]
distance = [[0]*m for _ in range(n)]

print(bfs(0,0))
