T_input = int(input())

for T in range(1, T_input + 1):
    a,b = map(int, input().split())

    diff = b-a

    if diff == 0:
        print(f"#{T} 0")
    
    elif diff < 0:
        print(f"#{T} -1")

    elif diff ==1:
        print(f"#{T} -1")

    else:
        if diff % 2 == 0:
            print(f"#{T} {diff//2}")

        else:
            print(f"#{T} {((diff-3)//2)+1}")