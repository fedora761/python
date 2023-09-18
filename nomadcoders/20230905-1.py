#data structures  4.0 ~ 4.4
#https://nomadcoders.co/python-for-beginners/lectures/3779
#python 표준 라이브러리: https://docs.python.org/ko/3/library/
#built-in Functions : https://docs.python.org/3/library/functions.html

#data structure

day_of_week = "Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday"
print(day_of_week)


#method는 데이터뒤에 결합/연결된function 이다
print("upper를 이용해 name 변수를 변경하기")
name ="nico"
print(name.upper())
print(name.capitalize())
print(name.startswith("e"))
print(name.startswith("n"))
print(name.replace("nico","dongjune"))
print(name.endswith("o"))

print()
print()
print("독릭적으로도 쓸수있다")
print("name".endswith("o"))
print("name".replace("n","😁"))

print()
print()
print()

#data에 적용가능한 method이다.
print("리스트에 결합된 메소드 만들기")

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(days_of_week.count("Wednesday"))

days_of_week.append("test1")
print(days_of_week)

days_of_week.append("test1")
print(days_of_week)

days_of_week.reverse()
print(days_of_week)

days_of_week.remove("Monday")
print(days_of_week)


days_of_week.clear()
print(days_of_week)

print("특정 리스트에 값 가져오기 / 컴터는 idx값이 0부터 시작")
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(days_of_week[0:3])
print(days_of_week[0])


print()
print()

#tuple 데이터 구조
#리스트는? 변수 = ["1","2","3"] / tuple은? 변수 = ("1","2","3")
#튜플은 불변성을 가져 데티어를 변경하지 못한다, 개발할때 변수값이 변경되어도 상관없으면 리스트, 변경 못하게 하려면 tuple로 작성
days = ("Mon","Tue", "Wed")
print(days[0])
print(days[-1])

print()
print()
#Dicts / key value pair (키-값 쌍으로 만들어짐), 키는 단어이고 값은 정의이다 변수 = {"key":"value", "key":value, }
#딕셔너리는 많은 속성들을 가지고 있는 데이터를 만들때 쓰인다
player ={
    'name' : "David",
    'age' : 38,
    'faver_food' : ["🍔","🍕","🍟🍔"],
    "status" : "coworker"
}

print(player)
print(player.get("faver_food"))

player['xp'] = 3500
print(player)

player['faver_food'].append("🥤🧊")
print(player.get("faver_food"))


#Recap  
#https://nomadcoders.co/python-for-beginners/lectures/3783
#메소드 데이터에 연결된 결합된 function(함수), 데이터 안에 쓰는걸 이야기함

print("ex")
print("nico".upper())


number = [5,3,6,12,"test", 12, True]
number.append(["🍿","🍟🍔"])
print(number)
print(number[6])
print(number[-1]) #append를 선언하여서 제일 마지막 이모지가 출력됨
#number.clear()

#print("튜플")
#number = (5,3,6,12,"test", 12, True)

print()
print()
print("#원본 데이터")
player = {
    "name" :"David",
    "age" : 28,
    "fav_food" : ("🍗","🥩"),
    "friend" : {
        "name": "woojae",
        "age": 30,
        "fav_food": ["🌮"]
    }
}

print(player)
print()
print()
print("#데이터값 수정")
player['fav_food'] ='🍱'
player.pop("age") #key, value 삭제
player['friend']['fav_food'].append("🍜")

print(player)