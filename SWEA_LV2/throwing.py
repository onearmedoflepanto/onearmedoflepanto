T_input = int(input())

for T in range(1,T_input+1):
    N=int(input())
    arr=list(map(int, input().split()))
    arr_abs=list(map(abs, arr))

    min_value=min(arr_abs)
    count=arr_abs.count(min_value)

    print(f"#{T} {min_value} {count}")
