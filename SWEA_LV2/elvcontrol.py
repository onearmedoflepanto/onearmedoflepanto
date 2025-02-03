T_input = int(input())

for T in range(1,T_input+1):
    N,K=map(int, input().split())
    total_sum=0
    counter=0
    for i in range(1,N+1):
        if total_sum == K:
            counter=1
        total_sum+=i



    print(total_sum-counter)