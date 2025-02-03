'''
이 코드들은 코드업(codeup.kr)의 파이썬 기초 100제 풀이 코드입니다.
정답은 참고하지 않았고(문제를 풀어야 정답을 볼 수 있음) 전부 자력으로 풀었어용
'''

#문제 20~40(입력)

a=input()
b=input()
print(float(a)+float(b))

a=input()
b=int(a)
print('%x'%b)

a=input()
b=int(a,16)
print('%o'%b)

a=input()
b=ord(a)
print(b)

a=input()
b=int(a)
print(chr(b))

a=input()
b=-1*int(a)
print(b)

a=input()
b=ord(a)+1
print(chr(b))

a,b=input().split()
c=int(a)-int(b)
print(c)

a=input()
b=ord(a)+1
print(chr(b))

a,b=input().split()
c=int(a)-int(b)
print(c)

a,b=input().split()
c=float(a)*float(b)
print(c)

a,n=input().split()
print(a*int(n))

a,b=input().split()
print(int(a)**int(b))

a,b=input().split()
print(float(a)**float(b))

a,b=input().split()
print(int(a)//int(b))

a,b=input().split()
print(int(a)%int(b))

a=input()
print(format(float(a),".2f"))

a,b=input().split()
print(format(float(a)/float(b),".3f"))

a,b=input().split()

ar=int(a)
br=int(b)
print(ar+br)
print(ar-br)
print(ar*br)
print(ar//br)
print(ar%br)
print(format(ar/br,".2f"))
