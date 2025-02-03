T=int(input())

for Test_case in range(1,T+1):
    N=int(input())
    arr=[]
    for _ in range(N):
        char,repeater=input().split()
        repeater=int(repeater)
        temp=[]
        for i in range(repeater):
            temp.extend(char)
        arr.extend(temp)    

    print(f"#{Test_case}")

    for i in range(0, len(arr), 10):
        print("".join(arr[i:i+10]))