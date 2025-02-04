T_input = int(input())

for T in range(1, T_input + 1):
    valid = True
    chessboard = [[0] * 8 for _ in range(8)]
    count_rooks_total = 0


    for i in range(8):
        input_chessboard = input()
        count_rooks = input_chessboard.count("O")
        
        if count_rooks > 1:
            valid = False
            break

        elif count_rooks == 1:
            pos = input_chessboard.find("O")
            chessboard[i][pos] = 1
            count_rooks_total += count_rooks

    if valid:
        for j in range(8):
            column = [chessboard[i][j] for i in range(8)]
            if column.count(1) > 1:
                valid = False
                break

    if count_rooks_total != 8:
        print(f"#{T} no")
        continue

    if not valid:
        print(f"#{T} no")
        continue

    print(f"#{T} yes")