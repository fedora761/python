### 혼자 공부하는 파이썬 개정판 10-11강까지 완료 p102~ 111 완료

#숫자

##정수
##소수점이 없는 숫자
##10, 273, 52

##부동소수점
##소수점이 있는 숫자
## 10.1, 52.273, 52.0 

print (type(52))
print (type(52.0))

#숫자 연산자 덧셈: +, 뺄셈: -, 곱셈: *, 나눗셈: /, 정수나눗셈: // (몫), 나머지: %(소수점 아래를 날려버린다), 제곱: **
print()
print(10 + 10)
print(10 - 10)
print(10 * 10)
print(10 / 10)
print(10 % 3)
print(2 ** 2)
print(2 ** 3)
print(2 ** 4)
print (10 / 3)
print (10 // 3)

#정수 + 정수 = 정수
## !예외: 나눗셈

#부동소수점 + 부동소수점 = 부동소수점

#문자열+정수 !예외: "반복" *3 은 출력가능
#문자열 + 부동소수점 = 불가능

print()
# * / >>>> + - 
# 2 + (2*2) =  2 + 4   결과값 6 
print ((2*2)+2)

print()
#() 괄호연산자 ():계산이 먼저 일어나게 하는 기능
print((2+2)*2)

print()
print(4 **(1/2))
print(8 **(1/3))
print(16**(1/3))

print()
print("# 기본적인 연산")
print(15, "+", 4, '=', 15+4)
print(15, "-", 4, '=', 15-4)
print(15, "*", 4, '=', 15*4)
print(15, "/", 4, '=', 15/4)

print()
#3462를 17로 나누었을대의 몫과 나머지를 구하는 프로그램이다.
print ("- 몫:", 3462 // 17)
print ("- 나머지:", 3462 % 17 )

print()
print(2+2-2*2/2*2)
print(2-2+2/2*2+2)