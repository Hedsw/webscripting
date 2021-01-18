import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = "https://stackoverflow.com/jobs?q=python"

def get_lage_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
    last_page = pages[-2].get_text(strip=True)
    return int(last_page)

def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f"{URL}&pg={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class":"-job"})
        for result in results:
            print(result["data-jobid"])

def get_jobs():
    last_page = get_lage_page()
    jobs = extract_jobs(last_page)
    return[]


# 2-9 StackOverFlow Pages 4:50초까지 봤음 영상 니콜라스 영상 
# https://nomadcoders.co/python-for-beginners/lectures/126