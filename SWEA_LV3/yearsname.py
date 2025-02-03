T_input = int(input())
for T in range(1, T_input+1):
    N, M = map(int, input().split())
    N_arr = input().split() 
    M_arr = input().split()    
    
    Q_input = int(input())
    result_arr = []
    
    for _ in range(Q_input):
        num = int(input())
        result = N_arr[(num - 1) % N] + M_arr[(num - 1) % M]
        result_arr.append(result)
    
    print(f"#{T}", end=' ')
    print(' '.join(result_arr))
