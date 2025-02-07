# import sys

# sys.stdin = open('sample_input,txt', 'r')

t_input=int(input())

for t in range(1,t_input+1):
    k, n, m = map(int, input().split())
    charge_stops=list(map(int, input().split()))

    stops=[0] + charge_stops + [n]

    distances=[]
    for i in range(1,len(stops)):
        distances.append(stops[i] -stops[i-1])

    if max(distances) > k:
        print(f"#{t} 0")
    
    else:
        charge_count = 0
        current_range = k
        last_stop = 0
        
        for i in range(1,len(stops)):
            if stops[i] - stops[last_stop] > k:
                charge_count +=1
                last_stop = i-1
                if stops[i] - stops[last_stop] > k:
                    charge_count = 0
                    break
    

        print(f"#{t} {charge_count}")