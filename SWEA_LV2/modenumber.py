T_input = int(input())

for T in range(1,T_input+1):
    N = int(input())
    arr=list(map(int, input().split()))

    count={}

    for item in arr:
        count[item] = count.get(item, 0) + 1

    max_count=max(count.values())

    mode=[key for key , value in count.items() if value == max_count]
    mode.sort()

    print(f"#{T} {mode[-1]}")