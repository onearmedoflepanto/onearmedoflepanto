def dfs(arr, score):
    global max_score
    if not arr:
        max_score = max(max_score, score)
        return
    
    for i in range(len(arr)):
        if len(arr) == 1:
            energy = arr[i]
        elif len(arr) == 2:
            energy = arr[1] if i == 0 else arr[0]
        else:
            if i == 0:
                energy = arr[1]
            elif i == len(arr) - 1:
                energy = arr[-2]
            else:
                energy = arr[i - 1] * arr[i + 1]
        
        new_arr = arr[:i] + arr[i+1:]
        dfs(new_arr, score + energy)


t_input = int(input())

for t in range(1,t_input+1):
    n = int(input())
    arr = list(map(int, input().split()))
    
    max_score = 0
    dfs(arr,0)

    print(f"#{t} {max_score}")
    