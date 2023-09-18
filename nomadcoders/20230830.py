# https://nomadcoders.co/python-for-beginners/lectures/3765
# 강의 진도 2.7 
# paramerter는 데이터를 저장하기 위한 placeholder(그릇)일뿐이다


print("니코가 만든 코드")
def say_hello(user_name, user_age): #user_name 변수 선언
    print("hello", user_name)
    print("you are", user_age, "years old") # 문자열+변수+문자열로 출력

say_hello("nico", 12)
say_hello("est", 13)

print()

print("2-8")
def tax_calculater(money):
    print(money * 0.35)

tax_calculater(1500000)
tax_calculater(150000)

print()
print()

print("2-9")
def say_hello(user_name):
    print("hello", user_name)
say_hello("nico")


print("user_name에 default값 넣기, agument에 값이 없어도 동작할수있게")

def say_hello(user_name="david"):
    print("hello", user_name)
say_hello()
print()

print("연습문제")

def plus(a=10,b=5):
    print(a+b)
    print(a-b)
    print(a/b)
    print(a*b)
    print(a**b)
plus (50, 4)

print()
print()

print("2-10")

def tax_calculater(money):
    print(money * 0.35)
tax_calculater(10)

print()

print("return값 받기")

def tax_cal(money):
    return money * 0.35

def pay_tax(tax):
    print("thank you for paying", tax)

to_pay = tax_cal (15000000)
pay_tax(to_pay)

print()
print()
print("return 변형")

def tax_cal(money):
    return money * 0.35

def pay_tax(tax):
    print("thank you for paying", tax)

pay_tax(tax_cal(1500000))

print()
print()
print("2-11강의")
my_name = "david"
my_age = 12
my_color_eyes ="brown"

print(f"hello I'm {my_name}, I have {my_age} years in the earth, {my_color_eyes} is my eye color")

print("hello I'm {my_name}, I have {my_age} years in the earth, {my_color_eyes} is my eye color")




print()
print()
print("juice maker")

def make_juice(fruit):
    return f"{fruit}+🥤"

def add_ice(juice):
    return f"{juice}+🧊"

def add_sugar(iced_juice):
    return f"{iced_juice}+🍬"

juice = make_juice("🍎")
cold_juice= add_ice (juice)
perfect_juice = add_sugar(cold_juice)

print(perfect_juice)

print("내가 짠 코드")

print()
print()

def berger(bigmac):
    return f"{bigmac}+🍔"

def potato(fried_potato):
    return f"{fried_potato}+🍟"

def drink(cola):
    return f"{cola}+🥤"

happy = berger("😋")
world = potato(happy)
time = drink(world)
macdonald = time

print(macdonald)