T_input = int(input())

for T in range(1,T_input+1):
    arr=list(map(int, input().split()))

    height_7th = max(arr)+1

    while height_7th<1000:
        arr.append(height_7th)
        if sum(arr)%7==0:
            break
        arr.pop()
        height_7th+=1

    print(height_7th)