#3. main.py -> wwr.py 사용하게 리펙토링

from requests import get
from bs4 import BeautifulSoup


def extract_wwr_jobs(keyword):
  base_url = "https://weworkremotely.com/remote-jobs/search?term="
  #search_key_word = "python"
  response = get(f"{base_url}{keyword}")
  if response.status_code != 200:
    print("can't open site")
  else:
    results = []
    soup = BeautifulSoup(response.text,
                         "html.parser")  #응답값을 response에 담고 html로 해석
    #print(soup.find_all('title')) #타이틀 찾아오는지 확인
    jobs = soup.find_all('section', class_="jobs")  #section에서 class=jobs를 찾아옴
    #print(len(jobs)) #몇개 jobs가 있는지 사이트와 비교 확인
    for job_section in jobs:
      job_posts = job_section.find_all('li')  #li 값만 추출
      job_posts.pop(-1)  #마지막 인덱스 삭제, li class="view-all"
      for post in job_posts:
        anchors = post.find_all('a')
        anchor = anchors[1]
        link = anchor['href']
        company, kind, location = anchor.find_all('span', class_='company')
        #find_all은 항상 리스트 형식을 줌
        title = anchor.find('span', class_='title')
        #print(company.string, kind.string, region.string,title.string)
        #.string을 통해 html 언어 제거
        job_data = {
            'company': company.string.strip().replace(",", " "),
            'location': location.string.strip().replace(",", " "),
            'position': title.string.strip().replace(",", " "),
            "link": f"https://weworkremotely.com{link}"
        }
        results.append(job_data)
    return results

  #for result in results:
  #print(result)
  #print("//////////")
