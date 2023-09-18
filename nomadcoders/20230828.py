# https://nomadcoders.co/python-for-beginners/lectures/3761
# 강의 진도 1.1 ~ 2.3

#출력
print("hello world!")

#Variables (변수)
a = 2
b = 3
c = a + b
#python code는 위에서 아래로 읽는다
a = 10
b = 15
print (c)
#7번 idx 에서에 c값을 정의했어서 변하지 않는다

print("옳은 변수값 만들기")
my_age = 88 #snake_case
MyAge = 88 #camel case
my_age1 = 88

#안되는 변수 유형 
# my age = 88  띄어쓰기 x 
# 123my_age = 88 숫자로 시작 x 
# /my_age = 88 특수기호 x

print()

print("data 타입")
#문자열값은 ""로 감싸야한다 
name = "DongJune"
print(name)

#boolean true or false
print("boolean")

name = True 
name = False
name ="True"#문자열로 만듬
print()


#연습
print("연습문제")
my_name = input("이름을 입력하세요: ")
age = input("나이를 입력하세요: ")
f = str(my_name)
g = int(age)
print("hello my name is", my_name, "and I'm", age, "years old")