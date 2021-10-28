import requests
from bs4 import BeautifulSoup

#构建网页
for i in range(6,11,1):
    for j in range(1,51,1):
        print(i)
        url = "https://baoava.com/vodtype/"+str(i)+"-"+str(j)+"/"
        print(url)
        r = requests.get(url)

        old_txt = "../old_data/sex/"+str(i)+"_"+str(j)+".txt"
        new_txt = "../data/sex/"+str(i)+"_"+str(j)+".txt"
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
