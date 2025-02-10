t_input = int(input())

for t in range(1,t_input+1):
    n = int(input())
    a=[]
    b=[]
    for _ in range(n):
        a_val, b_val = map(int,input().split())
        a.append(a_val)
        b.append(b_val)

    p = int(input())

    c=[]

    for _ in range(p):
        c_val = int(input())
        c.append(c_val)

    dat =[0] * 5001

    for i in range(n):
        for j in range(a[i], b[i]+1):
            dat[j] += 1

    print(f"#{t}",end=' ')
    for num in c:
        print(dat[num],end=' ')