# -*- coding:utf-8 -*-
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r"D:/chromedriver_win32/chromedriver.exe")
url = "https://5gamon.com/h/dalu/list_10_2.html"
driver.get(url)
driver.encoding = "utf-8"
#对于动态网页的时候一定要做到延迟。
time.sleep(5)
#这里面后期得判断一下是静态网页还是动态网页
soup = BeautifulSoup(driver.page_source)
a = soup.get_text()

print(a)
