T_input = int(input())

for T in range(1, T_input + 1):
    S = input()
    E = input()

    while len(E) > len(S):
        if E[-1] == 'X':
            E = E[:-1]
        elif E[-1] == 'Y':
            E = E[:-1]
            E = E[::-1]
    
    if E == S:
        print(f"#{T} Yes")
    else:
        print(f"#{T} No")
