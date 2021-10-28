import requests
from bs4 import BeautifulSoup

#构建网页

for j in range(1,51,1):
    url = "https://www.2b33699ffb5f597c.com/tupian/list-%E7%BE%8E%E8%85%BF%E4%B8%9D%E8%A2%9C-"+str(j)+".html"
    print(url)
    r = requests.get(url)
    r.encoding = "utf-8"

    old_txt = "../old_data/sex/"+"10"+"_"+str(j)+".txt"
    new_txt = "../data/sex/"+"10"+"_"+str(j)+".txt"
    print(old_txt)
    f1 = open(old_txt, "w", encoding="utf-8")

    soup = BeautifulSoup(r.text)
    a = soup.get_text().replace(" ","")
    f1.write(a)
    f1.close()

    with open(old_txt, "r", encoding='utf-8') as f2,open(new_txt, "w", encoding='utf-8') as fd:
        a = f2.readlines()
        for x in a:
            if x.strip():
                fd.write(x)

print("done")
