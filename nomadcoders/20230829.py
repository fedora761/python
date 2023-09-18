# https://nomadcoders.co/python-for-beginners/lectures/3765
# 강의 진도 2.4 - 2.6
# funtion (지속 재활용 가능) / ex: print(), 
print(True)
print("hello")
print(12)
print(True, "hello", 12)

#funtion을 만들때는 def로 정의, def 만들때는 숫자가 먼저나오면 규칙위반
#def 정의할때는 탭 or 스페이스바2번으로 함수내용 정의

def say_hello():
    print("hello how r u?")

def say_bye():
    print("bye bye")
    
say_hello()
say_bye()


#funtion을 만들때는 입력값을 받을수 있게 수정이 가능하다
#user_name는 parameter라고 부름
#user_name의 값은 argument라고 부름 funtion이 받는 데이터를 나타냄
print("니코가 만든 코드")
def say_hello(user_name): #user_name 변수 선언
    print("hello", user_name, "how r u?") # 문자열+변수+문자열로 출력

say_hello("nico")
say_hello("est")

print()
print()


print("내가 만든 코드")
user_name= input("이름을 입력해:")

def say_hello(user_name): #user_name 변수 선언
    print("hello", user_name, "how r u?") # 문자열+변수+문자열로 출력

say_hello(user_name)
    