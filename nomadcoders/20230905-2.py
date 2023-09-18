#data structures  4.5 ~ 4.9
#https://nomadcoders.co/python-for-beginners/lectures/3784
#python 표준 라이브러리: https://docs.python.org/ko/3/library/
#built-in Functions : https://docs.python.org/3/library/functions.html
#python packge: https://pypi.org/

#for loops 반복문
print("for loop에서 현재 실행중인 item 출력하기")
websites = {
    'google.com',
    'vivians.net',
    'estsoft.com'
}
for website in websites:
    print(website)


print()
print()
print("URL Formatting")

websites = {
    'https://google.com',
    'vivans.net',
}
for website in websites:
    if website.startswith("https://"):
        print("good to go")
    else:
        print("we have to fix it")



print()
print()
print("URL Formatting if not")

websites = {
    'https://google.com',
    'vivans.net'
}
for website in websites:
    if not website.startswith("https://"): # ==false 
        website = f"https://{website}"
    print(website)



print()
print()
print("Requests 테스트")

from requests import get

websites = {
    'https://google.com',
    'vivans.net',
    'nomadcoders.co', 
    'www.notion.so'
}

results ={}

for website in websites:
    if not website.startswith("https://"): # ==false 
        website = f"https://{website}"
    response = get(website)
    #print(response.status_code)
    if response.status_code ==200:
        #print(f"{website} is OK")
        results[website] ="OK"
    else:
        #print(f"{website} not OK")
        results[website] = "FAILED"

print(results)