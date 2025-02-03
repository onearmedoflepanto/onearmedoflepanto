Test_case=int(input())

for T in range(1,Test_case+1):
    N=int(input())
    arr=list(map(int,input().split()))

    for i in range(N):
        min_idx= i
        for j in range(i+1,N):
            if arr[j]<arr[min_idx]:
                min_idx= j

        arr[i], arr[min_idx] = arr[min_idx] , arr[i]

    print(f"#{T}",end=' ')
    print(*arr)