T_input = int(input())

for T in range(1,T_input+1):
    L,R = map(int, input().split())

    if (R+1)/2 > L:
        print("no")

    else:
        print("yes")