import requests
from bs4 import BeautifulSoup as bs

# URL = "https://stackoverflow.com/jobs?q=python"  # python이라는 단어로 검색했을 때 나오는 페이지 URL


def get_last_page(url):
    """ 마지막 페이지 알려주기"""
    result = requests.get(url)
    soup = bs(result.text, "html.parser")
    pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
    last_page = pages[-2].find("span").get_text(strip=True)
    return int(last_page)


def extract_job(html):
    """채용공고 하나에 있는 title, location, 회사명, id 가져오기"""

    title = html.find("h2", {"class": "mb4"}).find("a")["title"]
    company = html.find("h3", {"class": "fc-black-700"}).find_all("span")[0].get_text(strip=True)
    location = html.find("h3", {"class": "fc-black-700"}).find_all("span")[1].get_text(strip=True)
    job_id = html["data-jobid"]
    link = f"https://stackoverflow.com/jobs/{job_id}"

    return {"Title": title, "Company": company, "Location": location, "Link": link}


def extract_jobs(last_page, url):
    jobs = []
    for page in range(last_page):
        print(f"Scraping page {page+1}")
        result = requests.get(f"{url}&pg={page+1}")
        soup = bs(result.text, "html.parser")
        results = soup.find_all("div", {"class": "-job"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_jobs(word):
    url = "https://stackoverflow.com/jobs?q={word}"
    last_page = get_last_page(url)
    jobs = extract_jobs(last_page, url)
    return jobs
