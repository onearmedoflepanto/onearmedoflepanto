def boming(field,x,y):
    directions = [(-1,0),(1,0),(0,1),(0,-1),(-1,-1),(1,1),(-1,1),(1,-1)]
    for dx,dy in directions:
        nx,ny=x+dx,y+dy
        if 0<= nx <= 4 and 0<= ny <= 4:
            field[nx][ny] = "#"
    
    return field



field=[["_"]*5 for _ in range(5)]

x1,y1=map(int, input().split())
x2,y2=map(int, input().split())


field_1st=boming(field,x1,y1)

field_2nd=boming(field_1st,x2,y2)

for row in field_2nd:
    print(*row)