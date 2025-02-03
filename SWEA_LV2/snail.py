T=int(input())

for Test_case in range(1,T+1):
    N=int(input())

    matrix=[[0]*N for _ in range(N)]
    
    num=1

    top,bottom,left,right=0,N-1,0,N-1

    while left <= right and top <= bottom: 
        for col in range(left, right+1):
            matrix[top][col] = num
            num += 1
        top += 1
        
        for row in range(top, bottom+1):
            matrix[row][right] = num
            num += 1
        right -= 1
        
        if top <= bottom:
            for col in range(right, left-1, -1):
                matrix[bottom][col] = num
                num += 1
            bottom -= 1
        
        if left <= right:
            for row in range(bottom, top-1, -1):
                matrix[row][left] = num
                num += 1
            left += 1

    print(f"#{Test_case}")
    for row in range(N):
        print(*matrix[row])