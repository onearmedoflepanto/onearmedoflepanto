import math

T_input = int(input())

for T in range(1, T_input + 1):
    n = int(input())

    if n == 2:
        print(f"#{T} 1")
        continue

    if n == 3:
        print(f"#{T} 2")
        continue

    for i in range(int(math.sqrt(n)),0,-1):
        if n % i ==0:
            steps=i+(n//i)
            break


    print(f"#{T} {steps-2}")