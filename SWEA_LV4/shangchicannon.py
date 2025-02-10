t_input = int(input())

for t in range(1,t_input+1):
    n = int(input())

    board = [list(map(int, input().split())) for _ in range(n)]

    def cannonmove(x,y):
        global board
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        max_captures=0

        for dx,dy in directions:
            found_screen = False
            step = 1
            while True:
                nx = x + dx *step
                ny = y + dy *step

                if nx < 0 or nx > n or ny < 0 or ny > n:
                    break

                if not found_screen:
                    if board[nx][ny] != 0:
                        found_screen = True

                else:
                    if board[nx][ny] != 0:
                        if board[nx][ny] == 1:
                            board[nx][ny] = 0
                            captures = 1 + cannonmove(nx,ny)
                            max_captures = max(max_captures, captures)
                            board[nx][ny] = 1
                        break
                step += 1

        return max_captures
    
    cannonco=[(i,j) for i in range(n) for j in range(n) if board[i][j]==2]

    max_capture = cannonmove(cannonco[0][0],cannonco[0][1])
    print(f"{t} {max_capture}")