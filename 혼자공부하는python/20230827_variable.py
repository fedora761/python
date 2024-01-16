### 혼자 공부하는 파이썬 개정판 12-14강 완료 p112~ 133 완료
#값에 붙이는 이름

##변수를 만드는 방법
#식별자 = 값
# π  = 3.141592

#변수를 사용하는 방법
pi = 3.14592
print(pi)
print(pi+10)
print(pi*3)

#예x) 값 = 식별자
# 3.14592 = pi ->SyntaxError 발생

#변수와 관련된 용어
#정의 (선언) (define): 변수를 만드는 행위  
#할당 (assign): 변수에 값을 넣는 행위
#참조 (reference): 변수 안에 있는 값을 사용하는 행위

#정의와 할당
# pi = 3.141592 # python은 정의와 할당 동시에 진행함 

print()
pi = 3.14159265
r = 10
print("원주율=", pi)
print("반지름=", r)
print("원의 둘레=", 2 * pi * r)
print("원의 넓이=", pi * r * r)

print()
print()
#복합 대입 연산자
a=0
print(a)
a+=1 #a=a+1
print(a)
a -= 1 
print(a)
a += 1 
print(a)
print()

number = 100
number += 10
print (number)
number += 20
print (number)
number += 30
print (number)
print()


##형태
#[변수] [연산자] = [값]
#:변수에 값을 연산자해서 다시 변수에!

string = "안녕하세요!"
string += "!"
string += "!"
print(string)
print()
print()

#input()함수
#1. 프롬프트(입력을 요청하는 문자열)를 출역
#2.  사용자로부터 입력을 받을수 있게 일시정지
#3. 입력을 받으면 계속 진행 
input("입력해주세요: ")
print()

print(input("입력해주세요: "))
print()

a = input (">>>")
print(a)
#함수의 결과 = 함수의 리턴값 
print()

print("#인풋은 입력받은 값이 무조건 문자열로 나옴 // type로 결과 확인")
a = input (">>>")
print(a)
print(type(a))
print()

#input()함수
print("#입력받은 값이 문자열이라 숫자를 입력해도 문자+문자 형식으로 나옴")
a = input("숫자1: ")
b = input("숫자2: ")
print (a+b)


int("52") #정수
float("52.273") #부동소수점

#문자열 -> 숫자
print("#입력받은 값을 int형식으로 변경하는법")
a = input("숫자1: ")
b = input("숫자2: ")
a = int(a)
b = int(b)
print(a+b)

print("#int형식으로만 받으면 오류가 많이 날수도 있음 float(정수, 소수)형식으로 받기")
a = input("숫자1: ")
b = input("숫자2: ")
a = float(a)
b = float(b)
print(a+b)


#숫자 -> 문자열
c = str(a)
print(a+b)
print(c, type(c))




#확인문제
#1. = 

#2. +=, -=, *=, /=, %=, **=

#3. 문자열 int 자료형으로 변환 int(), float(), str()

#4. input, float

#5. input, float

