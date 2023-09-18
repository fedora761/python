#아래 배열의 숫자를 합하는 코드를 작성하고. 결과값을 프린트하세요.결과값은 136 이어야 합니다.
"""for item in list : for를 사용해 list([item0, item1, item2, ...])의 각 항목을 하나씩 item 변수로 루프
참고링크 - Python 공식문서
type() : 데이터 타입을 확인
is : ==와 같은 비교 연산자
if 조건문: 실행문 : 조건문이 참(True)일 때만 실행문 실행
"""
#https://reddb.tistory.com/85 파이썬 리스트 종류
#https://ssimplay.tistory.com/714 파이썬 for문으로 숫자 증가
#https://dojang.io/mod/page/view.php?id=2281 파이썬 리스트 조작하기
#https://corytips.tistory.com/162 파이썬 할당연산자

print("text 가져오기")
print()
print()
from requests import get 
from bs4 import BeautifulSoup

base_url = "https://www.vivans.net"
#search_term = "python"
#response = get(f"{base_url}{search_term}")
response = get(f"{base_url}")
print(response)
if response.status_code !=200:
    print("can't website read")
else:
    soup=BeautifulSoup(response.text, 'html.parser')
    #print(response.text)
    
"""
    #pip install selenium >>셀레니움 ( 브라우저 자동화 프로그램 ) 설치
#https://sites.google.com/chromium.org/driver/downloads >> 크롬 드라이버 설치

from requests import get
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options >>VSC환경에서는 옵션 변경 필요없음

# options = Options()
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")

# browser = webdriver.Chrome(options=options)
browser = webdriver.Chrome()

browser.get("https://kr.indeed.com/jobs?q=python")

print(browser.page_source)

>> 아래 내용이 없으면 실행된 코드가 종료되면서 브라우저 창이 같이 꺼지는데,
아래에 적힌 무한 루프를 이용해 프로그램이 끝나지 않게 하면 브라우저가 안 없어집니다.
브라우저가 잘 켜지는 것만 확인하고 나면, 주석 처리하시거나 삭제하셔도 됩니다.
# while (True):
# pass
"""
