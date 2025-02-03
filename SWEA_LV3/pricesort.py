T_input = int(input())
for T in range(1, T_input+1):
    N = int(input())
    arr = list(map(int, input().split()))
    result=[0]*N

    for i in range(N):
        result[i]=arr.pop(0)
        arr.remove((result[i]//3)*4)
        
    print(f"#{T}",end=' ')
    print(' '.join(map(str, result)))