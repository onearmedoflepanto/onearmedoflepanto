# arr=[list(map(int, input().split())) for _ in range(5)]


# counter=0
# arr_max=0
# arr_min=100
# diagnol_sum=0

# for i in range(5):
#     for j in range(5):
#         elem=arr[i][j]

#         if elem > arr_max:
#             arr_max = elem

#         if elem < arr_min:
#             arr_min = elem

#         if i == j:
#             diagnol_sum += elem

#         if elem == 2:
#             counter += 1

# print(counter)
# print(arr_max, arr_min)
# print(diagnol_sum)

# array = [
#     [1, 2, 1, 3, 1],
#     [2, 2, 2, 2, 2],
#     [1, 0, 1, 0, 1],
#     [3, 1, 2, 1, 3]
# ]

# x=1
# y=0

# sum_v=array[y][x-1]+ array[y][x+1]+ array[y+1][x]
# print(sum_v)

# x,y=map(int,input().split())

# grid = [
#     [1, 2, 1, 3, 1],
#     [2, 2, 2, 2, 2],
#     [1, 0, 1, 0, 1],
#     [3, 1, 2, 1, 3]
# ]

# directions=[(1,1),(-1,-1),(1,-1),(-1,1),(0,0)]
# diagnol_product=1

# for dx,dy in directions:
#     nx= x + dx
#     ny= y+ dy
#     diagnol_product *= grid[nx][ny]

# print(diagnol_product)




# for i in range(-k,k+1):
#         for j in range(-k,k+1):
#             directions.append((i,j))
#     for dx,dy in directions:
#         nx,ny=x+dx,y+dy
#         if 0<= nx < n and 0<= ny < m :
#             if field[nx][ny] != "#":
#                 field[nx][ny] = "%"
    
#     return field

# grid = [
#     [1, 2, 1, 3, 1],
#     [2, 2, 2, 2, 2],
#     [1, 0, 1, 0, 1],
#     [3, 1, 2, 1, 3]
# ]

# directions=[(1,1),(1,-1),(-1,1),(-1,-1)]

# sums=0
# x, y = map(int, input().split())
# for dx,dy in directions:
#     nx=x+dx
#     ny=y+dy

#     sums+=grid[nx][ny]

# print(sums)

grid = [
    [1, 2, 1, 3, 1],
    [2, 2, 2, 2, 2],
    [1, 0, 1, 0, 1],
    [3, 1, 2, 1, 3]
]

directions=[(1,1),(1,-1),(-1,1),(-1,-1)]

sums=0
x, y = map(int, input().split())
for dx,dy in directions:
    nx=x+dx
    ny=y+dy
    if nx>=0 and nx<5 and ny>=0 and ny<5:
        sums+=grid[nx][ny]


print(sums)