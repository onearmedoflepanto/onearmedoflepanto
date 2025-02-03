'''
이 코드들은 코드업(codeup.kr)의 파이썬 기초 100제 풀이 코드입니다.
정답은 참고하지 않았고(문제를 풀어야 정답을 볼 수 있음) 전부 자력으로 풀었어용
'''

#문제 85~90

...
86
입력
언제까지 합을 계산할 지, 정수 1개를 입력받는다.
단, 입력되는 자연수는 100,000,000이하이다.

출력
1, 2, 3, 4, 5 ... 순서대로 계속 더해가다가, 그 합이 입력된 정수보다 커지거나 같아지는 경우,
그때까지의 합을 출력한다.

...

w,h,b=input().split()
w=int(w)
h=int(h)
b=int(b)

iq=w*h*b/(8*1024*1024)

print(format(iq,".2f"),"MB")

#87
a=int(input())
for i in range(a+1):
    if i%3==0:
        continue
    print(i)

#88

...
입력
시작 값(a), 등차의 값(d), 몇 번째 수 인지를 의미하는 정수(n)가
공백을 두고 입력된다.(모두 0 ~ 100)

출력
n번째 수를 출력한다.
...

a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
d=a
for i in range(1,c):
   d=d+b
print(d)

#89

a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
d=a
for i in range(1,c):
   d=d*b
print(d)

...
입력
시작 값(a), 곱할 값(m), 더할 값(d), 몇 번째 인지를 나타내는 정수(n)가
공백을 두고 입력된다.(a, m, d는 -50 ~ +50, n은 10이하의 자연수)

출력
n번째 수를 출력한다.
...

a,m,d,n=input().split()
a=int(a)
m=int(m)
d=int(d)
n=int(n)
res=a
for i in range(1,n):
   res=res*m+d
print(res)
