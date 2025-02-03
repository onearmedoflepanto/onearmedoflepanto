T=int(input())

for Test_case in range(1,T+1):
    sudoku=[list(map(int, input().split()) for _ in range(9))]

    checker=1

    for row in sudoku:
        if len(set(row))!=9:
            checker=0

    for y in range(9):
        column=[sudoku[x][y] for x in range(9)]
        if len(set(column))!=9:
            checker=0

    for i in range(0,9,3):
        for j in range(0,9,3):
            block=[]
            for r in range(i,i+3):
                for c in range(j,j+3):
                    block.append(sudoku[r][c])
            
            if len(set(block))!=9:
                checker=0

    print(f"#{Test_case} {checker}")
