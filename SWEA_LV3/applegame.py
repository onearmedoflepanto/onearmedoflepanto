import sys

sys.stdin=open('input.txt', 'r')

T_input=int(input())

for T in range(1,T_input+1):
    n=int(input())
    arr=[list(map(int, input().split())) for _ in range(n)]
    
    m=0
    for i in range(n):
        max_row=max(arr[i])
        if max_row > m:
            m = max_row

    co_apples=[]

    for k in range(1,m+1):
        co_apple=[(i,j) for i in range(n) for j in range(m) if arr[i][j]==k]
        co_apples.append(co_apple)

    steps=0

    for l in range(len(co_apples)):
        if l == 0 and arr[0][0] == 0:
            continue
        else:
            steps +=1

        if l % 2 == 0:
            pass