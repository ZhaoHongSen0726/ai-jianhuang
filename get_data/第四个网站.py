# -*- coding:utf-8 -*-
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r"D:/chromedriver_win32/chromedriver.exe")


for j in range(451,551,1):
    url = "https://5gamon.com/h/rihan/list_3_"+ str(j) +".html"
    driver.get(url)
    driver.encoding = "utf-8"
    #对于动态网页的时候一定要做到延迟。
    time.sleep(5)
    #这里面后期得判断一下是静态网页还是动态网页
    soup = BeautifulSoup(driver.page_source)
    a = soup.get_text()

    old_txt = "../old_data/sex/" + "9" + "_" + str(j) + ".txt"
    new_txt = "../data/sex/" + "9" + "_" + str(j) + ".txt"
    print(old_txt)
    f1 = open(old_txt, "w", encoding="utf-8")

    f1.write(a)
    f1.close()

    with open(old_txt, "r", encoding='utf-8') as f2, open(new_txt, "w", encoding='utf-8') as fd:
        a = f2.readlines()
        for x in a:
            if x.strip():
                fd.write(x)
    #driver.close()

print("done")