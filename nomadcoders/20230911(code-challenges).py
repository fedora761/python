from requests import get
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}
base_url = "https://remoteok.com/remote-"
search_key_word = "python"
response = get(f"{base_url}{search_key_word}-jobs",headers=headers)
if response.status_code !=200:
    print("can't open site")
else:
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find_all('td', class_ = "company position company_and_position")
    jobs.pop(0)
    for list in jobs:
        title = list.find('h2',itemprop ='title')
        print("Title     :", (title.string).strip())
        name = list.find('h3',itemprop ='name')    
        print("Company   :", (name.string).strip())
        location = list.find_all('div',class_="location")
        for information_list in location:
            if "💰" in information_list.string:
                print("Salary    :", information_list.string)
            elif "⏰ " in information_list.string:
                print("Time      :", information_list.string)
            else:
                print("Region    :", information_list.string)
        herf = list.find_all('a')
        for link in herf:
            url = link.attrs["href"]
            print("link:",f"https://remoteok.com{url}")
        print()
        print("//////////////////////////netx job list///////////////////////////////////")
        print("//////////////////////////////////////////////////////////////////////////")    
        print()

            
"""    
    #jobs_tr = soup.find_all('tr') #section에서 class=jobs를 찾아옴
    #for jobs in jobs_tr:
    #    companys = jobs.find_all('td', class_ = "company position company_and_position")
    #    print(companys)
"""