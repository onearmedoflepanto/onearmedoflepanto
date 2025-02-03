T_input = int(input())

for T in range(1, T_input + 1):
    n = int(input())

    str=input()

    if n % 2 !=0:
        print(f"#{T} NO")

    elif str[:n//2] == str[n//2:]:
        print(f"#{T} YES")

    else:
        print(f"#{T} NO")
