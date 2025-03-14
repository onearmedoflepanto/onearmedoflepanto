def dfs(arr, score):
    global max_score
    newn = len(arr)
    if newn == 1:
        max_score = max(max_score, score + arr[0])
        return

    for i in range(newn):
        if i == 0:
            dfs(arr[1:], score + arr[1])

        elif i == newn - 1:
            dfs(arr[:-1], score + arr[-2])

        else:
            dfs(arr[:i] + arr[i+1:], score + arr[i-1] * arr[i+1])


tc = int(input())

for t in range(1, tc+1):
    n = int(input())
    arr = list(map(int, input().split()))
    max_score = 0
    dfs(arr, 0)
    print(f"#{t} {max_score}")
