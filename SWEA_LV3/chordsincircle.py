t_input=int(input())

for t in range(1,t_input+1):
    n=int(input())
    arr=map(int, input().split())
    possible_ab=[]

    for i in range(n):
        a = i
        possible_b = [num for num in range(n) if
                     num != a and abs(num-a) != 1 and
                     (a, num) != (0, n-1) and (a,num) != (n-1,0)]
        
        for b in possible_b:
            possible_ab.append((a,b))

    for a,b in possible_ab:
        possible_c = [num for num in range(n) if
                      num != a and num != b and
                      abs(num-a) != 1 and abs(num-b) != 1 and
                      (a==0 and num == n-1)]
        
        possible_d = [num for num in range(n) if
                      num != a and num != b and num != c and
                      abs(num-a != 1 and abs(num-b) != 1 and abs(num-1))]