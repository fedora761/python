#data structures  5.1 ~ 5.3
#https://nomadcoders.co/python-for-beginners/lectures/3784
#python 표준 라이브러리: https://docs.python.org/ko/3/library/
#built-in Functions : https://docs.python.org/3/library/functions.html
#python packge: https://pypi.org/

#https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term=python

print("200ok 가져오기")

from requests import get

#base_url = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="
base_url = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="
search_term = "python"
response = get(f"{base_url}{search_term}")
print(response)
print()
print()


print("text 가져오기")
print()
print()
from requests import get 
base_url = "https://weworkremotely.com/remote-jobs/search?search_uuid=&term="
search_term = "python"
response = get(f"{base_url}{search_term}")
if response.status_code !=200:
    print("Can't request website")
else:
    print(response.text)



print()
print()
print("beautifulsoap+ 리스트안에 loop 설정 for ~ in ~")
#https://nomadcoders.co/python-for-beginners/lectures/3794

from requests import get
from bs4 import BeautifulSoup


base_url = "www.naver.com"
search_key_word = "python"

response = get(f"{base_url}{search_key_word}")
if response.status_code !=200:
    print("동작을 하지 못합니다.")
else:
    soup = BeautifulSoup(response.text,'html.parser')
    jobs = print(soup.find_all('section', class_= "jobs"))
    #print(len(jobs))
    for job_section in jobs:
        job_posts = print(job_section.find_all('li'))
        job_posts.pop(-1) #라스트 항목을 삭제 -1 마지막
        for post in job_posts:
            print(post)
            print("////////////")
    
    
"""   
print()
print()
print("positional")

def say_hello(name, age):
    print(f"hello {name} you are {age} years old")

say_hello('nico',12)
#positional은 내가 어디에 어떤변수와 값이 오는줄 알고 있음
say_hello(name='nico', age=12)
""" 