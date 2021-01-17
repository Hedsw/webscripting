import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = "https://www.indeed.com/jobs?q=python&limit={LIMIT}"


# 2-9 StackOverFlow Pages 4:50초까지 봤음 영상 니콜라스 영상 
# https://nomadcoders.co/python-for-beginners/lectures/126