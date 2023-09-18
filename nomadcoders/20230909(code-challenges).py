#아래 배열의 숫자를 합하는 코드를 작성하고. 결과값을 프린트하세요.결과값은 136 이어야 합니다.
"""for item in list : for를 사용해 list([item0, item1, item2, ...])의 각 항목을 하나씩 item 변수로 루프
참고링크 - Python 공식문서
type() : 데이터 타입을 확인
is : ==와 같은 비교 연산자
if 조건문: 실행문 : 조건문이 참(True)일 때만 실행문 실행
"""
#https://reddb.tistory.com/85 파이썬 리스트 종류
#https://ssimplay.tistory.com/714 파이썬 for문으로 숫자 증가
#https://dojang.io/mod/page/view.php?id=2281 파이썬 리스트 조작하기
#https://corytips.tistory.com/162 파이썬 할당연산자


#numbers = [1, "💖", 2, "🔥", 3, "⭐️", 4, "💖", 5, "🔥", 6, "⭐️", 7, "💖", 8, "🔥", 9, "⭐️", 10, "💖", 11, "🔥", 12, "⭐️", 13, "💖", 14, "🔥", 15, "⭐️", 16]

"""
total = 0

# 리스트 순회하면서 숫자값만 더하기
for item in numbers:
    if isinstance(item, int):
        total += item

# 결과 출력
print("숫자값의 합:", total)
"""

numbers = [1, "💖", 2, "🔥", 3, "⭐️", 4, "💖", 5, "🔥", 6, "⭐️", 7, "💖", 8, "🔥", 9, "⭐️", 10, "💖", 11, "🔥", 12, "⭐️", 13, "💖", 14, "🔥", 15, "⭐️", 16]

# 숫자값을 저장할 변수 초기화
total_num = 0

# 리스트 순회하면서 숫자값만 더하고 타입 확인
for item in numbers:
    # 데이터 타입 확인
    data_type = type(item)
    print(data_type)
    # 조건문을 사용하여 숫자 값인지 확인
    if data_type == int:
        total_num += item

# 결과 출력
print("numbers의 합은:", total_num)


