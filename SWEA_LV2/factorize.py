T=int(input())

for Test_case in range(1,T+1):
    N=int(input())
    
    facts=[2,3,5,7,11]

    exp=[0]*5

    for i in range(5):
        while N % facts[i] == 0:
            exp[i] += 1
            N /= facts[i]

    print(f"#{Test_case}", end=' ')
    print(*exp)