def hanoimove(n,start=1,end=3,temp=2):
    if n==1:
        print(f"{n}번 디스크->{end}번 기둥")
        
    else:
        hanoimove(n-1,start,temp,end)
        print(f"{n}번 디스크->{end}번 기둥")
        hanoimove(n-1,temp,end,start)

n=int(input("하노이 탑의 갯수:"))
hanoimove(n)
