print("beautifulsoap+ 리스트안에 loop 설정 for ~ in ~")
#https://nomadcoders.co/python-for-beginners/lectures/3795
#5.1 ~ 5.10

#1 wwr 사이트 데이터 가지고 오기
"""
from requests import get
from bs4 import BeautifulSoup


base_url = "https://weworkremotely.com/remote-jobs/search?term="
search_key_word = "python"
response = get(f"{base_url}{search_key_word}")
if response.status_code !=200:
  print("can't open site")
else:
  soup = BeautifulSoup(response.text, "html.parser") #응답값을 response에 담고 html로 해석
  #print(soup.find_all('title')) #타이틀 찾아오는지 확인
  jobs = soup.find_all('section', class_ = "jobs") #section에서 class=jobs를 찾아옴
  #print(len(jobs)) #몇개 jobs가 있는지 사이트와 비교 확인
  for job_section in jobs:
    job_posts = job_section.find_all('li') #li 값만 추출
    job_posts.pop(-1) #마지막 인덱스 삭제, li class="view-all"
    for post in job_posts:
      print(post)
      print("//////////")

"""

"""
#2. wwr 사이트 데이터 상세 수정 - 1
from requests import get
from bs4 import BeautifulSoup


base_url = "https://weworkremotely.com/remote-jobs/search?term="
search_key_word = "python"
response = get(f"{base_url}{search_key_word}")
if response.status_code !=200:
  print("can't open site")
else:
  soup = BeautifulSoup(response.text, "html.parser") #응답값을 response에 담고 html로 해석
  #print(soup.find_all('title')) #타이틀 찾아오는지 확인
  jobs = soup.find_all('section', class_ = "jobs") #section에서 class=jobs를 찾아옴
  #print(len(jobs)) #몇개 jobs가 있는지 사이트와 비교 확인
  for job_section in jobs:
    job_posts = job_section.find_all('li') #li 값만 추출
    job_posts.pop(-1) #마지막 인덱스 삭제, li class="view-all"
    for post in job_posts:
      anchors = post.find_all('a') 
      anchor = anchors[1]
      link = anchor['href']
      company, kind, region = anchor.find_all('span', class_ = 'company')
      #find_all은 항상 리스트 형식을 줌
      title = anchor.find('span', class_ = 'title')
      print(company, kind, region,title)
      print("////////////////")
      print("////////////////")

"""


"""
HTML의 앵커 태그 즉, <a> 태그는 다른 페이지 또는 같은 페이지의 특정 위치나 파일과 같은 다른 URL로 연결할 수 있는 하이퍼링크를 만드는 기능을 한다. 우선 'anchor'라는 단어의 사전적 의미는 '닻을 내리다' '정박하다' '고정시키다' 라는 뜻이다

"""



#3. wwr 사이트 데이터 상세 수정 -2 html 문구 제외처리
#span 문구 처리
from requests import get
from bs4 import BeautifulSoup


base_url = "https://weworkremotely.com/remote-jobs/search?term="
search_key_word = "python"
response = get(f"{base_url}{search_key_word}")
if response.status_code !=200:
  print("can't open site")
else:
  results =[]
  soup = BeautifulSoup(response.text, "html.parser") #응답값을 response에 담고 html로 해석
  #print(soup.find_all('title')) #타이틀 찾아오는지 확인
  jobs = soup.find_all('section', class_ = "jobs") #section에서 class=jobs를 찾아옴
  #print(len(jobs)) #몇개 jobs가 있는지 사이트와 비교 확인
  for job_section in jobs:
    job_posts = job_section.find_all('li') #li 값만 추출
    job_posts.pop(-1) #마지막 인덱스 삭제, li class="view-all"
    for post in job_posts:
      anchors = post.find_all('a') 
      anchor = anchors[1]
      link = anchor['href']
      company, kind, region = anchor.find_all('span', class_ = 'company')
      #find_all은 항상 리스트 형식을 줌
      title = anchor.find('span', class_ = 'title')
      #print(company.string, kind.string, region.string,title.string)
      #.string을 통해 html 언어 제거
      job_data={
        'company': company.string,
        'region': region.string,
        'position': title.string
      }
      results.append(job_data)
  for result in results:
    print(result)
    print("//////////")    