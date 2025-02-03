T = int(input())
for t in range(1, T + 1):
    s = input().strip()
    
    if s != s[::-1]:
        print(f"#{t} NO")
        continue

    N = len(s)
    if N % 2 == 0:
        s_half = s[:N//2]
    else:
        s_half = s[:N//2]
    
    if s_half == s_half[::-1]:
        print(f"#{t} YES")
    else:
        print(f"#{t} NO")
