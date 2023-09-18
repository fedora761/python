from bs4 import BeautifulSoup
import requests


def extract_rmw_jobs(keyword):
  url = f"https://remoteok.com/remote-{keyword}-jobs"
  request = requests.get(url, headers={"User-Agent": "Kimchi"})
  results = []
  if request.status_code == 200:
    soup = BeautifulSoup(request.text, "html.parser")
    jobs = soup.find_all("tr", class_="job")
    for job in jobs:
      url = job.find('a')  #anchor를 전체 찾음
      link = url.attrs["href"]  #anchor에서 href만 찾음
      company = job.find("h3", itemprop="name")
      position = job.find("h2", itemprop="title")
      location = job.find("div", class_="location")
      if company:
        company = company.string.strip().replace(",", " ")
      if position:
        position = position.string.strip().replace(",", " ")
      if location:
        location = location.string.strip().replace(",", " ")
      if company and position and location:
        job = {
            'company': company,
            'position': position,
            'location': location,
            "link": f"https://remoteok.com/remote-jobs{link}"
        }
        results.append(job)
  else:
    print("Can't get jobs.")
  return results


"""
from bs4 import BeautifulSoup
import requests

def extract_rmw_jobs(keyword):
    url = f"https://remoteok.com/remote-{keyword}-jobs"
    request = requests.get(url, headers={"User-Agent": "Kimchi"})
    results = []
    if request.status_code == 200:
        soup = BeautifulSoup(request.text, "html.parser")
        jobs = soup.find_all("tr", class_="job")
        for job in jobs:
            company = job.find("h3", itemprop="name")
            position = job.find("h2", itemprop="title")
            location = job.find("div", class_="location")
            if company:
                company = company.string.strip().replace(","," ")
            if position:
                position = position.string.strip().replace(","," ")
            if location:
                location = location.string.strip().replace(","," ")
            if company and position and location:
                job = {
                    'company': company,
                    'position': position,
                    'location': location
                }
                results.append(job)
    else:
        print("Can't get jobs.")
    return results
"""
"""
#refactor rmw -> main.py

from requests import get
from bs4 import BeautifulSoup

def extract_rmw_jobs(keyword):
  headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}
  base_url = "https://remoteok.com/remote-"
  #search_key_word = "python"
  response = get(f"{base_url}{keyword}-jobs",headers=headers)
  if response.status_code !=200:
      print("can't open site")
  else:
      results = []
      soup = BeautifulSoup(response.text, "html.parser")
      jobs = soup.find_all('td', class_ = "company position company_and_position")
      jobs.pop(0)
      for list in jobs:
          title = list.find('h2',itemprop ='title')
          print("title     :", (title.string).strip())
          name = list.find('h3',itemprop ='name')    
          print("company   :", (name.string).strip())
          location = list.find_all('div',class_="location")
          for information_list in location:
              if "💰" in information_list.string:
                  print("salary    :", information_list.string)
              elif "⏰ " in information_list.string:
                  print("time      :", information_list.string)
              else:
                  print("location    :", information_list.string)
          herf = list.find_all('a')
          for url in herf:
              link = url.attrs["href"]
              print("link:",f"https://remoteok.com{link}")
      return results

        print()
          print("//////////////////////////netx job list///////////////////////////////////")
          print("//////////////////////////////////////////////////////////////////////////")    
          print()
            
"""
