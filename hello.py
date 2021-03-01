import dload
from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver')
driver.get("https://search.daum.net/search?nil_suggest=btn&w=img&DA=SBC&q=%EB%A5%98%EC%A7%84")
time.sleep(5)

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

thumbnails = soup.select("#imgList > div > a > img")

i = 1
for thumbnail in thumbnails:
    src = thumbnail["src"]
    dload.save(src, f'류진사진 크롤링/크롤링실습 {i}.jpg')
    i += 1

driver.quit()
