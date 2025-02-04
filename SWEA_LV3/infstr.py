import math

T_input = int(input())
for T in range(1, T_input+1):
    a, b =input().split()

    a_times=math.lcm(len(a),len(b))/len(a)
    b_times=math.lcm(len(a),len(b))/len(b)

    a_times=int(a_times)
    b_times=int(b_times)

    a_lcm = a * a_times
    b_lcm = b * b_times

    if a_lcm == b_lcm:
        print(f"{T} yes")
    
    else:
        print(f"{T} no")