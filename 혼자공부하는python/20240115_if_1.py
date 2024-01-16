### 혼자 공부하는 파이썬 개정판 19강 완료 p154 ~ p 완료
#03 불 자료형

#True 참, False 거짓, = 할당연산자, == 비교연산자
#단항 not , 이항 and or

"""
#둘다 True 일때 결과 True
print(True and True)   #true``
print(True and False)  #false
print(False and True)  #false
print(False and False) #false

#이항 or 
#둘중 하나만 True이면 결과 True
print(True or True)   #true``
print(True or False)  #false
print(False or True)  #false
print(False or False) #false
"""
print()
print()
print("날짜/시간 구하는 방법")
#날짜/시간 구하는 방법
import datetime
import pytz

seoul = pytz.timezone("Asia/Seoul")
now = datetime.datetime.now(seoul)
print(now)

print("{}년 {}월 {}일 {}시 {}분 {}초".format(
now.year,
now.month, 
now.day, 
now.hour,
now.minute,
now.second)
)

print()
print()
print("사용자가 입력한 숫자가 양수, 음수, 0인지 판별하는 프로그램")

#if 조건문
#사용자가 입력한 숫자가 양수, 음수, 0인지 판별하는 프로그램

#내가 작성한 코드
"""
user = float(input("숫자만 입력하세요: "))

if user > 0:
    print(f'입력값은 {user}이며 양수입니다.')

elif user < 0:
    print(f'입력값은 {user}이며 음수입니다.')

else:
    print(f'입력값은 {user}이며 0입니다.')
"""

#강의 결과
raw_input = input("숫자를 입력하세요: ")
raw_input = int(raw_input)

if raw_input > 0:
    print("양수입니다.!")

if raw_input < 0:
    print("음수입니다.!")

if raw_input == 0:
    print("0입니다.!")


print()
print()
print("오전 오후 구분 프로그램")
#오전 오후 구분하는 프로그램
from pytz import timezone
from datetime import datetime
today = datetime.now(timezone('Asia/Seoul'))

print(f"{today.hour}시 입니다.")

if today.hour < 12:
    print("오전입니다.!")

if today.hour >= 12:
    print("오후입니다.!")


print()
print()
print("계절을 구분하는 프로그램")
#계절을 구분하는 프로그램
from pytz import timezone
from datetime import datetime
today = datetime.now(timezone('Asia/Seoul'))

m = today.month

if 3 <= m <=5:
    print(f"현재는 {m}월 이며, 봄입니다!")

if 6 <= m <=8:
    print(f"현재는 {m}월 이며, 여름입니다!")

if 9 <= m <=11:
    print(f"현재는 {m}월 이며, 가을입니다!")  

if (11 <= m <=12) or (m ==1):
    print(f"현재는 {m}월 이며, 겨울입니다!") 


print()
print()
print("짝수 홀수 구하는 프로그램 -1")
#짝수 홀수 구하는 프로그램 -1
raw = input("정수를 입력해주세요: ")
l = raw[-1]

"""
if l == "0" or l == "2" or l == "4" or l == "6" or l == "8":
    print("짝수입니다.")

if l == "1" or l == "3" or l == "5" or l == "7" or l == "9":
    print("홀수입니다.")
"""

if l in "02458":
    print("짝수입니다.")

if l in "13579":
    print("홀수입니다.")



print()
print()
print("짝수 홀수 구하는 프로그램 -2")
#짝수 홀수 구하는 프로그램 -2
raw = input("정수를 입력해주세요: ")
raw = int(raw)

if raw % 2 == 0:  #%2로 나누었을때 몫이 0일경우
    print("짝수입니다.")

if raw % 2 == 1: #%2로 나누었을때 몫이 1일경우
    print("홀수입니다.")
