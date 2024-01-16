### 혼자 공부하는 파이썬 개정판 19강 ~25강 완료 p154 ~ p203 완료
#if문만 사용시 전 if문을 다 비교함
#elif, else를 사용하면 스텝이 줄어드는 효과가 있어 코드 시간 및 리소스 절약이 가능함

#홀수 짝수 구분

print("홀수 짝수 구분")
number = int(input("정수 입력:"))
if number % 2 == 0:
    print("짝수입니다.")
else: #if number % 2 == 1:
    print("홀수입니다.")

print()
print()

print("오전 오후 구분")
from pytz import timezone
from datetime import datetime
today = datetime.now(timezone('Asia/Seoul'))

if today.hour < 12:
    print(f"현재 시간은 {today.hour}시 이며, 오전입니다.")

else: #if today.hour >= 12:
    print(f"현재 시간은 {today.hour}시 이며, 오후입니다.")

print()
print()
#양수 음수 0인가?
print("양수 음수 0인가")

number = int(input("정수입력: "))
if number > 0:
    print(f"입력값은 {number}이며, 양수입니다")
elif number < 0:
    print(f"입력값은 {number}이며, 음수입니다")
else:
    print(f"입력값은 {number}이며, 0입니다")


print()
print()
#봄 여름 가을 겨울
print("봄 여름 가을 겨울")

month = int(input("월 입력:"))
if 3 <= month <= 5:
    print("봄입니다.")
elif 6 <= month <= 8:
    print("여름입니다.")
elif 9 <= month <= 10:
    print("가을입니다.")
else:
    print("겨울입니다.")


print()
print()
print("학점 성적표")
#학점 성적표

score = float(input("학적을 입력해주세요: "))

if score == 4.5:
    print(f"입력 학점은 {score}입니다. 축하합니다. 당신은 신입니다.")
elif 4.2 <= score:
    print(f"입력 학점은 {score}입니다. 축하합니다. 당신은 교수님의 사랑을 받았습니다.")
elif 3.5 <= score:
    print(f"입력 학점은 {score}입니다. 축하합니다. 당신은 교수님의 사랑을 받았습니다.")
elif 3.5 <= score:
    print(f"입력 학점은 {score}입니다. 축하합니다. 당신은 교수님의 사랑을 받았습니다.")
elif 2.8 <= score:
    print(f"입력 학점은 {score}입니다. 축하합니다. 당신은 평균 점수를 받았습니다.")
else:
    print(f"입력 학점은 {score}입니다. 다음학기에는 공부를 해야합니다.")




print()
print()
print("태어난 띠 확인하기")
#띠 확인하기

str_input = input("태어난 해를 입력해주세요: ")
birth_yrar = int(str_input)

print(("원숭이,닭,개,돼지,쥐,소,범,토끼,용,뱀,말,양").split(",") [birth_yrar % 12], "띠 입니다.")
"""
if birth_yrar % 12 == 0:
    print("원숭이 띠입니다.")

if birth_yrar % 12 == 1:
    print("닭 띠입니다.")

if birth_yrar % 12 == 2:
    print("개 띠입니다.")

if birth_yrar % 12 == 3:
    print("돼지 띠입니다.")

if birth_yrar % 12 == 4:
    print("쥐 띠입니다.")

if birth_yrar % 12 == 5:
    print("소 띠입니다.")

if birth_yrar % 12 == 6:
    print("범 띠입니다.")

if birth_yrar % 12 == 7:
    print("토끼 띠입니다.")

if birth_yrar % 12 == 8:
    print("용 띠입니다.")

if birth_yrar % 12 == 9:
    print("뱀 띠입니다.")

if birth_yrar % 12 == 10:
    print("말 띠입니다.")
if birth_yrar % 12 == 11:
    print("양 띠입니다.")
"""