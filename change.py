Test_case=int(input())

for T in range(1,Test_case+1):
    list_money=[50000,10000,5000,1000,500,100,50,10]

    N=int(input())
    result=[]

    for money in list_money:
        count= N//money
        result.append(count)
        N-=count*money
    
    print(f"#{T}")
    print(*result)