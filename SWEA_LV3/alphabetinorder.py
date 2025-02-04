T_input = int(input())

for T in range(1, T_input + 1):
    str_input = input()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    counter = 0

    for i in range(len(str_input)):
        if str_input[i] == alphabet[i]:
            counter += 1
        else:
            break

    print(f"#{T} {counter}")