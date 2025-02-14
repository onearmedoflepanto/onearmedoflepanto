t_input = int(input())

for t in range(1,t_input+1):
    flag = True
    n, k = map(int, input().split())

    sample = list(map(int, input().split()))
    passcode = list(map(int, input().split()))

    sample = str(sample)
    passcode = str(passcode)

    idx = sample.find(passcode[0])

    if idx == -1:
        print(f"#{t} 0")
        flag = False
        continue

    for i in range(len(passcode)):
        idx = sample.find(passcode[i], idx)
        if idx == -1:
            print(f"#{t} 0")
            flag = False
            break
    
    if flag:
        print(f"#{t} 1")