def dfs(x,y):
    if not (0<= x <n and 0<= y <m):
        return 0
    
    if visited[x][y] or field[x][y] == 1:
        return 0

    visited[x][y] = True
    
    count = 1
    directions = [(1,0),(-1,0),(0,1),(1,1)]

    for dx, dy in directions:
        count += dfs(x+dx, y+dy)
    return count

field =[[0,0,1,1,0],[0,0,0,1,1],[1,1,1,1,1],[0,0,0,0,0]]
n= len(field)
m= len(field[0])
visited = [[False]*m for _ in range(n)]

max_size = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j] and field[i][j] != 1:
            max_size = max(max_size,dfs(i,j))

print(max_size)