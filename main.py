# add -> commit
# git push -u origin main

from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

option = Options()
option.add_argument("disable-infobars")
option.add_argument("disable-extensions")
option.add_argument('disable-gpu')
#option.add_argument('headless')

browser = webdriver.Chrome('./chromedriver', options=option)
browser.get('https://play.google.com/store/apps/details?id=com.lottemembers.android&hl=ko&gl=US')

html = browser.page_source
soup = bs(html,"html.parser")

browser.findElement(By.xpath('//*[@id="ow2107"]/section/div/div/div[5]/div/div/button')).click();

reviews = soup.select('div.h3YV2d')
print (len(reviews))
for r in reviews:
    print (r, r.text)