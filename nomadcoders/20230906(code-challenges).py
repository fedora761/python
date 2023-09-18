monthly_revenue = 5500000
monthly_expenses = 2700000
tax_credits = 0.01 
#세금 공제

def get_yearly_revenue():
    return monthly_revenue * 12
print ("월간 매출은", monthly_revenue,"이며 년간 매출은", get_yearly_revenue(), "입니다.")

def get_yearly_expenses():
    return monthly_expenses * 12
print ("월간 비용은", monthly_expenses, "이며 년간 매출은", get_yearly_expenses(), "입니다.")

profit = get_yearly_revenue() - get_yearly_expenses()
print("년간 이익은", profit, "입니다.")

#print(type(profit))
#만약 (if) profit이 100,000 초과이면. 세율은 25% 이다. 아닌 경우에는 (else). 세율은 15% 이다.

def get_tax_amount(profit):
    if profit > 100000:
        return profit * 0.25
    else:
        profit * 0.15

tax_amount=get_tax_amount(profit)

#print("세율은",tax_amount,"입니다.")

#tax_amount = get_tax_amount()

def apply_tax_credits():
    return tax_amount * tax_credits

final_tax_amount = tax_amount - apply_tax_credits()

print(f"Your tax bill is: ${final_tax_amount}")


"""
if user_choise == pc_choise:
    print("you won")
elif user_choise < pc_choise:
    print("Higher!!! Computer Chose", pc_choise)
elif user_choise > pc_choise:
    print("Lower!! Computer chose", pc_choise)
    

    
"""
"""
def say_nick(nick):
	if nick == "바보":
    		return
    	print("나의 별명은 %s입니다." % nick)
    https://velog.io/@cha-suyeon/Python-%ED%95%A8%EC%88%98%EC%97%90%EC%84%9C-return%EC%9D%98-%EC%93%B0%EC%9E%84
"""


"""
1. get_yearly_revenue (연간 매출 계산)
monthly_revenue (월간 매출)를 인수로 받고, revenue for a year (연간 매출)를 리턴.
takes monthly_revenue and returns revenue for a year.

2. get_yearly_expenses (연간 비용 계산)
monthly_expenses (월간 비용)를 인수로 받고, expenses for a year (연간 비용)를 리턴.
takes monthly_expenses returns expenses for a year.

3. get_tax_amount (세금 계산)
profit (이익) 를 인수로 받고, tax_amount (세금 금액) 를 리턴.
takes profit returns tax_amount.

4. apply_tax_credits (세액 공제 적용)
tax_amount (세금 금액), tax_credits (세액 공제율)를 인수로 받고, amount to discount (할인할 금액)를 리턴.
takes tax_amount and tax_credits returns amount to discount.
Requirements (요구사항)
get_tax_amount 함수는 if/else 를 사용해야한다.
만약 (if) profit이 100,000 초과이면. 세율은 25% 이다.
아닌 경우에는 (else). 세율은 15% 이다.

get_yearly_revenue : 월간매출를 인자로 받아서 연간매출을 리턴하는 함수
get_yearly_expenses : 월간비용를 인자로 받아서 연간비용을 리턴하는 함수
get_tax_amount : 이익을 인자로 받아서, 이익이 100,000보다 크면 25% 세율을 적용하고, 크지 않으면 15% 세율을 적용해서 세금금액을 리턴하는 함수
apply_tax_credits : 세금금액. 세액공제율을 인자로 받아서, 공제할 금액을 리턴하는 함수

"""

"""
print("return값 받기")

def tax_cal(money):
    return money * 0.35

def pay_tax(tax):
    print("thank you for paying", tax)

to_pay = tax_cal (15000000)
pay_tax(to_pay

"""
