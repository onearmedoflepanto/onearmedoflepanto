import sys
sys.stdin = open("input.txt", "r")

T_input = int(input())

for T in range(1,T_input+1):
    N = int(input())

    commands=[list(map(int, input().split())) for _ in range(N)]
    speed=0
    distance=0

    for row in range(len(commands)):
        if commands[row][0] == 0:
            pass

        elif commands[row][0] == 1:
            speed+=commands[row][1]


        else:
            speed-=commands[row][1]

        if speed<0:
            speed=0

        distance+=speed

    print(f"#{T} {distance}")