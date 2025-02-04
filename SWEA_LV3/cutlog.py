T_input = int(input())

for T in range(1, T_input + 1):
    n = int(input())

    if n % 2 == 0:
        print(f"#{T} Alice")

    else:
        print(f"#{T} Bob")