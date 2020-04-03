import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://jp.indeed.com/%E6%B1%82%E4%BA%BA?q=python&l=%E5%A4%A7%E9%98%AA%E5%BA%9C&limit={LIMIT}"

def extract_indeed_pages():
  indeed_result =  requests.get(URL)

  indeed_soup = BeautifulSoup(indeed_result.text,"html.parser")

  pagination = indeed_soup.find("div",{"class":"pagination"})

  pages = pagination.find_all("a")
  spans = []
  for page in pages[:-1]:
    spans.append(int(page.find("span").string))

  max_page = spans[-1]
  return max_page

def extract_jobs(html):

    title = html.find("div",{"class":"title"}).find("a")["title"]
    price_tag = html.find("div",{"class":"salarySnippet"})
    price = ""
    if price_tag is not None:
      price = price_tag.find("span",{"class":"salaryText"}).string
      price = price.strip()
    else:
      price= "未記入"

    location_tag = html.find("span",{"class":"location"})
    location = location_tag.string
    
    company_tag = html.find("span",{"class":"company"})
    company = company_tag.string
    job_id = html["data-jk"]
    return {
      'title':title,
      'price':price,
      'company':company,
      'location':location,
      'link':f"https://jp.indeed.com/viewjob?jk={job_id}"
    }
    
    
def extract_indeed_jobs(last_page):
  jobs =[]
  for page in range(last_page):
    print(f"Scrapping page {page}")
    result = requests.get(f"{URL}&start={page*LIMIT}")
    
    indeed_soup = BeautifulSoup(result.text,"html.parser")
    job_cards = indeed_soup.find_all("div",{"class":"jobsearch-SerpJobCard"})
  
    for result in job_cards:
      job = extract_jobs(result)
      jobs.append(job)

  return jobs
    # print(jobs)

    