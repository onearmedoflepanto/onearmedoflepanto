T_input = int(input())

for T in range(1,T_input+1):
    N=int(input())
    counter=0
    seen_digits=set()
    while len(seen_digits)<10:
        counter+=1
        currnet_value=N*counter
        seen_digits.update(str(currnet_value))

    print(f"#{T} {currnet_value}")