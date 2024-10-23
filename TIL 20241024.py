'''
이 코드들은 코드업(codeup.kr)의 파이썬 기초 100제 풀이 코드입니다.
정답은 참고하지 않았고(문제를 풀어야 정답을 볼 수 있음) 전부 자력으로 풀었어용
'''

#문제 80~5

a,b=input().split()
a=int(a)
b=int(b)
for i in range(1,a+1):
    for j in range(1,b+1):
        print(i,j)

a=input()
a=int(a,16)
for i in range(1,16):
    print('%X'%a,"*",'%X'%i,"=",'%X'%(a*i),sep='')

a=int(input())
j=0

for i in range(1,a+1):
    if i%3==0 and i<=10:
        print("X")
    elif i>10 and i<=20 and (i-10)%3==0:
        print("X")
    elif i>20 and (i-20)%3==0:
        print("X")
    else:
        print(i)

a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
d=0
for i in range(0,a):
    for j in range(0,b):
        for k in range(0,c):
            print(i,j,k)
            d+=1
print(d)

h,b,c,s=input().split()
h=int(h)
b=int(b)
c=int(c)
s=int(s)

iq=h*b*c*s/(8*1024*1024)

print(format(iq,".1f"),"MB")

w,h,b=input().split()
w=int(w)
h=int(h)
b=int(b)

...
입력
w, h, b 가 공백을 두고 입력된다.
단, w, h는 모두 정수이고 1~1024 이다. b는 40이하의 4의 배수이다.
 

출력
필요한 저장 공간을 MB 단위로 바꾸어 출력한다.
단, 소수점 셋째 자리에서 반올림하여 둘째 자리까지 출력한다.
...

iq=w*h*b/(8*1024*1024)

print(format(iq,".2f"),"MB")
