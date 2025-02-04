T_input = int(input().strip())

for T in range(1, T_input + 1):
    arr = input()
    
    visible = sum(1 for ch in arr if ch in "()")
    
    pair_count = 0
    i = 0
    while i < len(arr) - 1:
        if arr[i] == '(' and arr[i+1] == ')':
            pair_count += 1
            i += 2
        else:
            i += 1

    print(f"{T} {visible - pair_count}")
