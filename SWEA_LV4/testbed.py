def isprime(n):
    if n < 2 or n in [2, 3] or n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i**2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False

        i += 6
    return True


tc = int(input())

for t in range(tc):
    n = int(input())

    if n % 2 == 0:
        n += 1

    if isprime(n):
        print(n)
    else:
        while not isprime(n):
            n += 2

        print(n)
