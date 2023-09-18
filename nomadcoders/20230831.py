#if문  3.0 ~ 3.7
#https://nomadcoders.co/python-for-beginners/lectures/3771

print("조건문 기본")

if 10 > 5:
    print("correct!")

if 13 <= 10:
    print("True!")

if 10 == 10:
    print("True!")

a = 10
if a==10:
    print("True!")

a = "nico"
if a=="nico":
    print("True!")

print()
print()
print("if & else")

password_correct = False
if password_correct:
    print("Here is your money")
else:
    print("Wrong password")


print()
print()
print("elif")

winner = 5
if winner > 10:
    print("Winner is greater than 10")
elif winner < 10:
    print("Winner is less than 10")
else: 
    print("Winner is 10")

print()
print()
print("if,else,elif")
#else는 if, elif 둘다 포함되지 않을때 제일 마지막에 호출된다
winner = 40
if winner > 100:
    print("If")

elif winner ==10:
    print("Elif1")

elif winner < 30:
    print("Elif2")

elif winner > 50:
    print("Elif3")

else:
    print("Else") 

print()
print()
print("And & or", "and는 한 줄에 두가지 조건을 확인 가능")
print("음주계산기 만들기")

age = int(input("How old are you?"))
#print(type(age))
if age < 18:
    print("you can't drink.")
elif age >= 18 and age <= 35:
    print("we'll service potato")
elif age == 60 or age == 70:
    print("Birthday party!") 
else:
    print("Go ahead!")

# True and True == True
# False and True == False
# True and False == False
# False and False == False

# True or True == True
# True or False == True
# True or False == True
# False or False == False
""" #주석처리
print()
print()
print("python casino")

user_choise = int(input("choose number"))

pc_choise = 50

if user_choise == pc_choise:
    print("you won")
elif user_choise < pc_choise:
    print("Higher!!!")
elif user_choise > pc_choise:
    print("Lower!!")

""" 

print()
print()
print("python library")
print("python casino1, python random number")

from random import randint
#python random의 randint를 임포트하자
#built-in Functions : https://docs.python.org/3/library/functions.html
user_choise = int(input("choose number"))

pc_choise = randint(1,50)

if user_choise == pc_choise:
    print("you won")
elif user_choise < pc_choise:
    print("Higher!!! Computer Chose", pc_choise)
elif user_choise > pc_choise:
    print("Lower!! Computer chose", pc_choise)

print()
print()
print("while", "+1 증가값은 while 문 아래에 있어야 적용이 됨")

distance = 0

while distance <=20:
    print("I'm running:", distance, "km")
    distance = distance +1


"""
print()
print()
print("lotto")

from random import randint 
pc_choice = randint (1,45)

user_chois = (input("어서오세요: 로또 추첨기입니다. 무작위 숫자를 원하시면 random 을 입력하세요"))

user_chois = True 

if user_chois == str:
    print("로또 번호를 출력합니다:", pc_choise)
    
    while pc_choice <= 6:
        pc_choice = pc_choice +1
"""


print("while python casino")
#python random의 randint를 임포트하자
#built-in Functions : https://docs.python.org/3/library/functions.html

from random import randint

pc_choise = randint(1,50)
playing = True

while playing: 
    user_choise = int(input("choose number"))
    if user_choise == pc_choise:
        print("you won")
        playing = False
    elif user_choise < pc_choise:
        print("Higher!!!")
    elif user_choise > pc_choise:
        print("Lower!!")

