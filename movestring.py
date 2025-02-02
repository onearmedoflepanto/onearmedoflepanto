# T_input = int(input())

# for T in range(1,T_input+1):
#     string=input()
#     K=int(input())
#     cals=list(map(int, input().split()))

#     for cal in cals:
#         shift=cal % len(string)
#         string = string[-shift:] + string[:-shift]
#         print(string)

T_input = int(input())

for T in range(1, T_input + 1):
    string = input()
    K = int(input())
    cals = list(map(int, input().split()))

    for cal in cals:
        shift = abs(cal) % len(string)

        if cal > 0:
            string=string[shift:]+string[:shift]

        else:
            string=string[-shift:]+string[:-shift]
    
    print(string)
