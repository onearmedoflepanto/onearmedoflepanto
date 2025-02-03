T_input = int(input())

for T in range(1, T_input + 1):
    n=int(input())
    counter = 0

    for i in range(-n,n+1):
        for j in range(-n,n+1):
            if i**2 + j**2 <= n**2:
                counter +=1

    print(f"#{T} {counter}")