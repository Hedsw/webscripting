import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = "https://stackoverflow.com/jobs?q=python"

def get_lage_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
    print(pages)

def get_jobs():
    last_page = get_lage_page()
    return[]


# 2-9 StackOverFlow Pages 4:50초까지 봤음 영상 니콜라스 영상 
# https://nomadcoders.co/python-for-beginners/lectures/126