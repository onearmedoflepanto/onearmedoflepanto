t_input = int(input())

for t in range(1, t_input+1):
    ax1, ay1, ax2, ay2 = map(int, input().split())
    bx1, by1, bx2, by2 = map(int, input().split())

    if ax1 < bx1 < ax2:
        xcondition = 0

    elif ax1 == bx1 or ax2 == bx1:
        xcondition = 1

    else:
        xcondition = 2

    if ay1 < by1 < ay2:
        ycondition = 0

    elif ay1 == by1 or ay2 == by1:
        ycondition = 1

    else:
        ycondition = 2

    coditions=[[1,2,4],
               [2,3,4],
               [4,4,4]]
    
    print(xcondition,ycondition)
    
    print(f"#{t} {coditions[xcondition][ycondition]}")