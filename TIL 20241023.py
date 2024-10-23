'''
이 코드들은 코드업(codeup.kr)의 파이썬 기초 100제 풀이 코드입니다.
정답은 참고하지 않았고(문제를 풀어야 정답을 볼 수 있음) 전부 자력으로 풀었어용
'''

#문제 70~80

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

a=1

while a!=0:
    a=int(input())
    if a!=0:
        print(a)

a=int(input())

while a!=0:
    print(a)
    a-=1

a=int(input())

while a!=0:
    a-=1
    print(a)

a=ord(input())
b=ord('a')
while b!=a+1:
    print(chr(b))
    b+=1

a=int(input())
b=0
while b!=a+1:
    print(b)
    b+=1

a=int(input())
for i in range(a+1):
    print(i)

n = int(input())
s = 0
for i in range(1, n+1) :
  if i%2==0 :
    s=s+i
    
print(s)

a=input()
while a!="q":
    print(a)
    a=input()
print(a)

a=int(input())
j=1
i=0
while j<=a:
    j=j+i
    i+=1
if j<=a:
    print(i)
else:
    print(i-1)


a,b=input().split()
a=int(a)
b=int(b)
for i in range(1,a+1):
    for j in range(1,b+1):
        print(i,j)


