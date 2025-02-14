grid = [
    [1, 2, 1, 3, 1],
    [2, 2, 2, 2, 2],
    [1, 0, 1, 0, 1],
    [3, 1, 2, 1, 3]
]



directions=[(0,1),(0,-1),(1,0),(1,1)]

max_v = 0
x, y = map(int, input().split())


for dx,dy in directions:
    nx=x+dx
    ny=y+dy
    if 0<= nx <4 and 0<= ny <5:
        if max_v < grid[nx][ny]:
            max_v = grid[nx][ny]
    

print(max_v)
