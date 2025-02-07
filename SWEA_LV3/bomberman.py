n,m=map(int,input().split())

k=int(input())

field_input=[input() for _ in range(n)]

field=[[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        field[i][j]=field_input[i][j]


def boming(field,x,y,k):
    global m,n
    direncitons=[(-1, 0), (1, 0), (0, -1), (0, 1),(0,0)]
    for dx,dy in direncitons:
        for dist in range(1,k+1):
            nx,ny= x+dx*dist, y+dy*dist
            
            if not (0<= nx < n and 0<= ny < m):
                break

            if field[nx][ny] == "#":
                break
            
            field[nx][ny] = "%"
    
    return field

co_bombs=[]

for i in range(n):
    for j in range(m):
        if field[i][j] == "@":
            co_bombs.append((i,j))

for x,y in co_bombs:
    field = boming(field,x,y,k)

for row in field:
    print(''.join(row))