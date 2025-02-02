
counter=1
arr=[[0]*3 for _ in range(3)]

for i in range(3):
    for j in range(3):
        arr[i][j]=counter
        counter+=1
        print(arr)