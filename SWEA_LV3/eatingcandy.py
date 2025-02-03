T = int(input())
for t in range(1, T + 1):
    A, B, C = map(int, input().split())
    
    if C < 3 or B < 2:
        print(f"#{t} -1")
        continue

    B_prime = min(B, C - 1)
    A_prime = min(A, B_prime - 1)
    

    decrease_sum = (A - A_prime) + (B - B_prime)
    print(f"#{t} {decrease_sum}")
