t_input = int(input())

for t in range(1, t_input + 1):
    n = int(input())
    target = [None] + list(map(int, input().split()))
    
    bulbs = [0] * (n + 1)
    counter = 0
    
    for i in range(1, n + 1):
        if bulbs[i] != target[i]:
            for j in range(i, n + 1, i):
                bulbs[j] = 1 - bulbs[j]  
            counter += 1 
    
    print(f"#{t} {counter}")