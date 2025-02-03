Test_case=int(input())

for T in range(1,Test_case+1):
    N,M = map(int,input().split())
    arrA=list(map(int,input().split()))
    arrB=list(map(int,input().split()))

    if N > M:
        N,M = M,N
        arrA,arrB = arrB,arrA

    max_sumAB=0

    for i in range(M-N+1):
        sumAB=0
        for j in range(N):
            sumAB+=arrA[j]*arrB[i+j]

        if sumAB > max_sumAB:
            max_sumAB = sumAB

    print(f"#{T} {max_sumAB}")