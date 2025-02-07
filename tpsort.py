import sys
sys.stdin = open("input.txt", "r")

T_input = int(input())
for _ in range(T_input):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    counter = 0
    for i in range(N, 0, -1):
        if arr[i-1][0] != (i-1) * N + 1:
            counter += 1
            for j in range(i):
                for k in range(j + 1, i):
                    arr[j][k], arr[k][j] = arr[k][j], arr[j][k]
    
    print(counter)