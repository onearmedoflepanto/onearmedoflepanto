T_input = int(input())

results = [[1, 0, 1], [0, 1, 0]]

for T in range(1, T_input + 1):
    s, K = input().split()
    K = int(K)
    pos_cup = s.index("o")
    
    if K == 0:
        print(f"#{T} {pos_cup}")
    else:
        k_mod = K % 2 
        print(f"#{T} {results[k_mod-1][pos_cup]}")