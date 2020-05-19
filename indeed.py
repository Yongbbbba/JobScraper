import requests
from bs4 import BeautifulSoup as bs

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"  # python이라는 단어로 검색했을 때 나오는 페이지 URL

# 함수명이 좀 구리다. 바꿔야겠다 나중에.


def get_last_page():
    """마지막 페이지 가져오기, 총 페이지 수가 얼마나 되는지 확인하는 과정"""

    result = requests.get(URL)
    soup = bs(result.text, "html.parser")

    paginiation = soup.find("div", {"class": "pagination"})

    links = paginiation.find_all("a")
    pages = []
    for link in links[:-1]:
        pages.append(int(link.find("span").string))
    max_page = max(pages)
    return max_page


def extract_job(html):
    """ 해당 채용 공고의 제목, 회사, 주소, id와 지원 페이지링크 가져오기"""

    title = html.find("h2", {"class": "title"}).find("a")["title"]  # title 속성의 속성값 가져오기

    if html.find("span", {"class": "company"}) == None:
        company = "None"
    else:
        company = html.find("span", {"class": "company"}).get_text(strip=True)

    location = html.find("span", {"class": "location"}).get_text(strip=True)
    job_id = html["data-jk"]
    link = f"https://www.indeed.com/viewjob?jk={job_id}"

    return {"Title": title, "Company": company, "Location": location, "Link": link}


def extract_jobs(last_page):
    """ 모든 페이지의 채용공고 긁어오기 """

    jobs = []
    for page in range(last_page):
        print(f"Scraping page {page+1}")
        result = requests.get(f"{URL}&start={page*LIMIT}")
        soup = bs(result.text, "html.parser")
        results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
        for result in results:
            job = extract_job(result)

            jobs.append(job)

    return jobs


def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs
