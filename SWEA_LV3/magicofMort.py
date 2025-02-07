n=int(input())

field=[list(map(int, input().split())) for _ in range(n)]

k=int(input())

def magic(field,x,y,k):
    global n
    directions=[]
    kills=0
    for i in range(1,k+1):
        dicrection=[(i,i),(i,-i),(-i,i),(-i,-i)]
        directions.extend(dicrection)
    for dx,dy in directions:
        nx,ny=x+dx,y+dy
        if 0<= nx < n and 0<= ny < n :
            kills += field[nx][ny]

    return kills

kills_max=0

for i in range(n):
    for j in range(n):
        kills=magic(field,i,j,k)
        if kills > kills_max:
            kills_max = kills

print(kills_max)