t_input = int(input())

for t in range(1,t_input+1):
    n, p = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(n)]

    directions=[(1,0),(-1,0),(0,1),(0,-1)]

    def bomb(board,x,y):
        sum_total = 0
        
        for dx,dy in directions:
            for pow in range(1, p+1):
                nx = x+dx*pow
                ny = y+dy*pow

                if 0<= nx <n and 0<= ny <n:
                    sum_total += board[nx][ny]


        sum_total += board[x][y]
        return sum_total
    
    max_v = 0

    for i in range(n):
        for j in range(n):
            val = bomb(arr, i , j)
            if val > max_v:
                max_v = val

    print(f"#{t} {max_v}")