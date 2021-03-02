from bs4 import BeautifulSoup
from selenium import webdriver
from openpyxl import Workbook

driver = webdriver.Chrome('chromedriver')
driver.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%BD%94%EB%A1%9C%EB%82%98")

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

wb = Workbook()
ws1 = wb.active
ws1.title = "articles"
ws1.append(["제목", "링크", "신문사", "썸네일"])

articles = soup.select("#main_pack > section.sc_new.sp_nnews._prs_nws > div > div.group_news > ul > li")
for article in articles:
    a_tag = article.select_one("div.news_wrap.api_ani_send > div > a")

    title = a_tag.text
    url = a_tag['href']
    comp = article.select_one("div.news_wrap.api_ani_send > div > div.news_info > div > a.info.press").text.split(' ')[0].replace('언론사', ' ')
    thumbnail = article.select_one("div.news_wrap.api_ani_send > a > img")['src']
    print(title, url, comp, thumbnail)
    ws1.append([title, url, comp, thumbnail])

driver.quit()
wb.save(filename='articles.xlsx')