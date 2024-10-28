'''
이 코드들은 코드업(codeup.kr)의 파이썬 기초 100제 풀이 코드입니다.
정답은 참고하지 않았고(문제를 풀어야 정답을 볼 수 있음) 전부 자력으로 풀었어용
'''

#문제 91~94

...

...
입력
같은 날 동시에 가입한 인원 3명이 규칙적으로 방문하는,
방문 주기가 공백을 두고 입력된다. (단, 입력값은 100이하의 자연수이다.)

출력
3명이 다시 모두 함께 방문해 문제를 풀어보는 날(동시 가입/등업 후 며칠 후?)을 출력한다.
...

a,b,c=input().split()

a=int(a)
b=int(b)
c=int(c)

for i in range(max(a,b,c),a*b*c+1):
    if i%a==0 and i%b==0 and i%c==0:
        print(i)
        break

#92

...
입력
첫 번째 줄에 출석 번호를 부른 횟수인 정수 n이 입력된다. (1 ~ 10000)
두 번째 줄에는 무작위로 부른 n개의 번호(1 ~ 23)가 공백을 두고 순서대로 입력된다.

출력
1번부터 번호가 불린 횟수를 순서대로 공백으로 구분하여 한 줄로 출력한다.
...

n=int(input())
a=input().split()

for i in range(n):
    a[i]=int(a[i])

d=[]

for i in range(24):
    d.append(0)

for i in range(n):
    d[a[i]]+=1
    
for i in range(1,24):
    print(d[i],end=' ')


#93

...
입력
번호를 부른 횟수(n, 1 ~ 10000)가 첫 줄에 입력된다.
n개의 랜덤 번호(k, 1 ~ 23)가 두 번째 줄에 공백을 사이에 두고 순서대로 입력된다.

출력
출석을 부른 번호 순서를 바꾸어 공백을 두고 출력한다.
...

n=int(input())

a=input().split()

for i in range(n-1,-1,-1):
    print(a[i],end=' ')

#94
...
입력
번호를 부른 횟수(n, 1 ~ 10000)가 첫 줄에 입력된다.
n개의 랜덤 번호(k)가 두 번째 줄에 공백을 사이에 두고 순서대로 입력된다.

출력
출석을 부른 번호 중에 가장 빠른 번호를 출력한다.
...

n=int(input())

a=input().split()

for i in range(0,n-1):
    a[i]=int(a[i])

mintemp=int(a[0])

for i in range(0,n-1):
    if mintemp>int(a[i+1]):
        mintemp=a[i+1]
        
print(mintemp)
