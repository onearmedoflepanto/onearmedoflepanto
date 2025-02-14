import math
import sys

sys.stdin = open("input.txt", "r")

def distance(a,b):
    x1,y1=a
    x2,y2=b

    return (abs(x1-x2))**2 + (abs(y1-y2))**2

t_input = int(input())

for t in range(1, t_input+1):
    n = int(input())

    n += 1

    arr= [list(map(int, input().split())) for _ in range(n)]

    repeater_co = [(i,j) for i in range(n) for j in range(n) if arr[i][j] == 2]

    repeater_co = repeater_co[0]

    house_co = [(i,j) for i in range(n) for j in range(n) if arr[i][j] == 1]

    radius_max = 0

    for house in house_co:
        radius = distance(house, repeater_co)
        if radius > radius_max:
            radius_max = radius

    print(f"#{t} {int(math.ceil(math.sqrt(radius_max)))}")