from bs4 import BeautifulSoup
import requests
import time
print('Put some skills that are unfamilier for you')
unfamilier_skills=input('>')
print(f'filtering out {unfamilier_skills}')

def find_jobs():
    html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=data+science&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
            posted_date=job.find('span', class_='sim-posted').text
            if "few" in posted_date:
                company_name = job.find('h3', class_= 'joblist-comp-name').text.replace(' ','')
                skills_sep=job.find('div', class_='srp-skills').text.strip()
                skills=(', '.join(skills_sep.split()))
                more_info = job.a['href']
                if unfamilier_skills not in skills:
                    with open(f'posts/{index}.txt', 'w') as f:
                        f.write(f"company name: {company_name.strip()}\n")
                        f.write(f"skills: {skills}\n")               
                        f.write(f"posted data: {posted_date.strip()}\n")
                        f.write(f"more info: {more_info}")
                        print(f'File saved: {index}')

if __name__ == '__main__':
     while True:
          find_jobs()
          time_wait=10
          print(f'waiting {time_wait} minutes')
          time.sleep(time_wait * 60)