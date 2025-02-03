'''
이 코드들은 코드업(codeup.kr)의 파이썬 기초 100제 풀이 코드입니다.
정답은 참고하지 않았고(문제를 풀어야 정답을 볼 수 있음) 전부 자력으로 풀었어용
'''

#문제 60~70

a,b=input().split()
print(a!=b)

a,b=input().split()
print(int(a)|int(b))

a,b=input().split()
print(int(a)^int(b))

a,b=input().split()
print(int(a) if(int(a)>int(b)) else int(b))

ar,br,cr=input().split()
a=int(ar)
b=int(br)
c=int(cr)
print((a if (a<b) else b) if ((a if (a<b) else b)<c) else c)

ar,br,cr=input().split()
a=int(ar)
b=int(br)
c=int(cr)
if a%2==0:
    print(a)
if b%2==0:
    print(b)
if c%2==0:
    print(c)

ar,br,cr=input().split()
a=int(ar)
b=int(br)
c=int(cr)
if a%2==0:
    print("even")
else:
    print("odd")
if b%2==0:
    print("even")
else:
    print("odd")
if c%2==0:
    print("even")
else:
    print("odd")

ar,br,cr=input().split()
a=int(ar)
b=int(br)
c=int(cr)
if a%2==0:
    print(a)
if b%2==0:
    print(b)
if c%2==0:
    print(c)

ar=input()
a=int(ar)
if a<0:
    if a%2==0:
        print("A")
    else:
        print("B")
else:
    if a%2==0:
        print("C")
    else:
        print("D")

a=int(input())

if a>=90:
    print("A")
else:
    if a>=70:
        print("B")
    else:
        if a>=40:
            print("C")
        else:
            print("D")


a=input()

if a=="A":
    print("best!!!")
else:
    if a=="B":
        print("good!!")
    else:
        if a=="C":
            print("run!")
        else:
            if a=="D":
                print("slowly~")
            else:
                print("what?")

a=int(input())

if a//3==1 :
    print("spring")
else:
    if a//3==2:
        print("summer")
    else:
        if a//3==3:
            print("fall")
        else:
            print("winter")
