
print("계산기 만들어보기")


while True:
    user_number1 = int(input("Choose a number: "))
    user_number2 = int(input("choose another one: "))
    user_choise = input("choose an operation: \n Options are : +, -, * or /  \n Write 'exit' to finish. : ")
    if  user_choise == "exit":
        print("계산기를 종료합니다.")
        break
    elif user_choise == "+":
        print()
        print("계산값은", user_number1 + user_number2, "입니다.")
        print()
    elif user_choise == "-":
        print("계산값은", user_number1 - user_number2, "입니다.")
        print()	
    elif user_choise == "*":
        print("계산값은",user_number1 * user_number2, "입니다.")	
        print()
    else: 
        print("계산값은",user_number1 / user_number2, "입니다.")	


