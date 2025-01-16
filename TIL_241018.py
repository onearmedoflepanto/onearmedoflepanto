'''
이 코드들은 코드업(codeup.kr)의 파이썬 기초 100제 풀이 코드입니다.
정답은 참고하지 않았고(문제를 풀어야 정답을 볼 수 있음) 전부 자력으로 풀었어용
'''

#문제 40~60

a,b=input().split()
print(int(a)//int(b))

a,b=input().split()
print(int(a)%int(b))

a=input()
print(format(float(a),".2f"))

a,b=input().split()

ar=int(a)
br=int(b)
print(ar+br)
print(ar-br)
print(ar*br)
print(ar//br)
print(ar%br)
print(format(ar/br,".2f"))

a,b,c=input().split()
print(int(a)+int(b)+int(c), format((int(a)+int(b)+int(c))/3,".2f"))

a=input()
print(int(a)<<1)

a,b=input().split()
print(int(a)<<int(b))

a,b=input().split()
print(int(a)<int(b))

a,b=input().split()
print(a==b)

a,b=input().split()
print(int(b)>=int(a))

a,b=input().split()
print(a!=b)

a=input()
print(int(a)!=0)

a=input()
print(not bool(int(a)))

a,b=input().split()
print(bool(int(a)) and bool(int(b)))

a,b=input().split()
print(bool(int(a))^bool(int(b)))

a,b=input().split()
print(bool(int(a))==bool(int(b)))

a,b=input().split()
print(not (bool(int(a)) or bool(int(b))))

a=input()
print(~int(a))

a,b=input().split()
print(int(a)&int(b))
