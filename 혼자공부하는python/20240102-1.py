### 혼자 공부하는 파이썬 개정판 15~18강 완료 p134 ~ p153 완료
#02-4 숫자와 문자열의 다양한 기능

#기존에 배운것
a = 52
b = 273
#52 + 273 = {더한값}
print (a,"+", b,"=", a+b)

c = str(a) + "+" + str(b) + "=" + str(a+b)
print(c)

print()
print()

#format 함수
print("{}".format(10))
print("{} {}".format(10,20))
print("{}년 {}월 {}일".format(2024, 1, 2))

#위 예제 변경하기
print("{} + {} = {}".format(a, b, a+b))
#format함수는 틀을 만들어서 틀안의 값을 표현하는 함수이다.

print()
print()

#format 함수 사용시 실수하는 부분, 틀과 값은 일치하게 만드는게 중요
"""
print("#테스트1")
print("{}".format(10,20,30))

print()
print()

print("#테스트2")
print("{}{}".format(10))
"""

#split 함수

print("10 20 30 40".split(" "))
print("10-20-30-40".split("-"))
print("10/20/30/40".split("/"))
print("10         20\t30\n40".split()) #괄호를 생략하면 공백 (띄어쓰기, 줄바꿈, 탭문자등)으로 자릅니다.


# f문자열

c = 100
d = 200

print("{} + {} = {}".format(c,d, c+d))
print(f"{c} + {d} = {c+d}")

print()
print()

#f문자열은 여러줄 문자열에서도 사용가능

print(f"""{c}+{d} = {c+d}
{c}-{d} = {c-d}
{c}*{d} = {c*d}
""")

print()
print()


#확인문제
#3번 다음 코드의 빈칸을 채워서 실행 결과처럼 춣력해 보세요.
#결과값 100+200+300

#책내용
a = (input("> 1번째 숫자: "))
b = (input("> 2번째 숫지: "))
print()

print("{}+{}={}".format(a,b,int(a)+int(b)))
print(f"{a}+{b}={int(a)+int(b)}")



#동준 수정
a = int(input("> 1번째 숫자: "))
b = int(input("> 2번째 숫지: "))
print()

print("{}+{}={}".format(a,b,a+b))
print(f"{a}+{b}={a+b}")


print()
print()


print("도전문제1")

#입력: 반지름 입력
r = input("반지름: ")
r = float(r)

#처리: 부피 + 겉넓이
pi = 3.141592
부피 = (4/3) * pi * (r ** 3)
겉넓이 = 4 * pi * (r**2)

# 출력
print(f"부피: {부피}")
print(f"겉넓이: {겉넓이}")



print()
print()


print("도전문제2")
#입력:  밑변 + 높이
a = input("밑변을 입력하시오: ")
a = float(a)

b = input("높이를 입력하시오: ")
b = float(b)

#처리: 빗변
c = ((a**2) + (b**2)) **(1/2)

#출력
print(f"밑변값은 {a}이고, 높이값은 {b}이다. 빗변은 {c}이다.")
