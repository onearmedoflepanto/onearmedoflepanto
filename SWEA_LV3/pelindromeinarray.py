def is_palindrome(word):
    return word == word[::-1]

t_input = int(input())
for t in range(1, t_input+1):
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]

    palindrome=''

    for rows in arr:
        for i in range(len(rows) - m + 1):
            if is_palindrome(rows[i:i+m]):
                palindrome = ''.join(rows[i:i+m])
                break
        if palindrome:
            break

    # 세로 방향 검사
    if not palindrome:
        for j in range(len(arr[0])):
            column = [arr[x][j] for x in range(n)]
            for i in range(len(column) - m + 1):
                if is_palindrome(column[i:i+m]):
                    palindrome = ''.join(column[i:i+m])
                    break
            if palindrome:
                break
    
    print(f"#{t} {palindrome}")