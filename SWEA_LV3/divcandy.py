T_input = int(input())

for T in range(1, T_input + 1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    A.sort()
    diff_maxmin = float('inf')

    for i in range(N-K+1):
        current_diff = A[i+K-1] - A[i]
        
        if current_diff < diff_maxmin:
            diff_maxmin = current_diff

    print(f"#{T} {diff_maxmin}")