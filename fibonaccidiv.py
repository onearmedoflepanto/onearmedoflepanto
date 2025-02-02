def fibonacci(n):
    if n==1 or n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
T_input = int(input())

for T in range(1,T_input+1):
    N = int(input())

    if N % 3 == 2:
        print("BA",end='')
        for _ in range(N//3):
            print("BBA",end='')
    elif N % 3 == 0:
        for _ in range(N//3):
            print("BBA",end='')
    else:
        print("impossible",end='')

    print()