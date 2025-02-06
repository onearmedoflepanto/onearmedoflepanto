T_input=int(input())

for T in range(1,T_input+1):
    n,m1,m2 = map(int, input().split())

    arr = list(map(int, input().split()))

    arr.sort(reverse=True)

    rank_list=list(range(1,m1+1))+list(range(1,m2+1))
    rank_list.sort()

    price_total=0

    for i in range(n):
        price_total += arr[i] * rank_list[i]

    print(f"#{T} {price_total}")
