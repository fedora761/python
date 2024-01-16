### 혼자 공부하는 파이썬 개정판 15~18강 완료 p134 ~ p153 완료
#02-4 숫자와 문자열의 다양한 기능

# + 연산자: 피연산자를 바꾸지 않음
# 비파괴적이다
a = 10
a + 10
a + 20
a + 30

print(a)

print()
print()

# = 연산자: 피연산자를 바꿈!
# 파괴적이다
a  = 10
a  = 20
a  = 30

print(a)

print()
print()

# 문자열도 동일하게 적용

a = "안 녕 하 세 요"
a.split
a.upper
a.count

print(a)

print()
print()

a = "안 녕 하 세 요"
a = a.split( )
print(a)

a= "hello"
a = a.upper() #대문자로 변경
print(a)


a="HELLO"
a = a.lower() #소문자로 변경
print(a)

print()
print()

#strip 함수 양쪽 공백을 삭제
a = "     안녕하세요  \t \n \n  "
print(a)

a = a.strip()
print(a)
#a.lstrip()
#a.rstrip()


print()
print()

#is00()함수 결과로 맞다, 아니다를 출력
print("is00()함수 결과로 맞다, 아니다를 출력")
a = "안녕하세요"
a = a.isalpha()
#a = a.isdigit()
#a = a.isspace()
print(a)

#b = "안녕"
#print(b.isalpha())


a = "abcdabcd"
#find, rfind
#왼쪽부터 탐색: 1번째
print(a.find("b"))

#오른쪽부터 탐색: 5번째
print(a.rfind("b"))


#in 연산자 / 앞에 있는것이 뒤에 있는가를 찾는 함수
print("안녕" in "안녕하세요")
print("잘가" in "안녕하세요")

print()
print()

print("눈도장~~~")
#정수
print("{:d}".format(52))

#특정 칸 만큼 출력
print("{:5d}".format(52))
print("{:10d}".format(52))

print("{:05d}".format(52))
print("{:010d}".format(52))

#부호
print("{:5d}".format(52))
print("{:5d}".format(-52))

print("{:=5d}".format(52))
print("{:=5d}".format(-52))

print("{:=+5d}".format(52))
print("{:=+5d}".format(-52))

#소수점 출력
print("{:=+20.3f}".format(52))
print("{:=+20.1f}".format(52))
print("{:=+20.2f}".format(-52))