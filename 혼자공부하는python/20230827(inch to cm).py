#inch 단위를 cm 단위로 변경하기
#입력: inch 단위를 입력
a= input("inch 단위숫자:" )


# 처리: inch -> cm 변환처리
a = float(a) * 2.54

#출력: cm 단위를 출력
print("cm 단위로는", a, "입니다")

print()
print()

#inch 단위를 cm 단위로 변경하기
#입력: inch 단위를 입력
a= input("inch 단위숫자:" )
a = float(a)

# 처리: inch -> cm 변환처리
a =  a * 2.54

#출력: cm 단위를 출력
print("cm 단위로는", a, "입니다")


#원의 반지름 구하기 테스트
print("원의 반지름 구하기")

str_input = input("원의 반지름 입력>" )
num_input = float(str_input)
print()
print("반지름:", num_input)
print("둘레: ", 2 * 3.14 * num_input)
print("넓이: ", 3.14 * num_input ** 2)




#해설
print("원의 반지름 구하기 해설")
#입력: 반지름입력
r = input("반지름:")
r = float(r)

#처리: 둘레와 넓이를 구한다
pi = 3.14
둘레 = 2 * pi * r
넓이 = pi * (r **2)

#출력: 둘레와 넓이를 출력한다
print("둘레:", 둘레)
print("넓이:", 넓이)



#6 문자열 두개를 입력받고 다음과 같이 출력하는 ...

#https://pythontutor.com/  통해서 확인
print("문자열 두개 입력, 출력")
#입력: 반지름입력
a = input("문자열 입력:" )
b = input("문자열 입력:" ) 
#a = str(a)
#b = str(b)
#str = (a,b)

#print(a,b)
#print(b,a)

print(a,b)

c = a
a = b
b = c

print(a,b)


print(type(a))


