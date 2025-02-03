T_input = int(input())

for T in range(1, T_input + 1):
    a,b,c = map(int, input().split())

    d = a+c - 2*b

    if d==0:
        print(f"#{T} 0.0")

    else:
        print(f"#{T} {abs(d)/4}")