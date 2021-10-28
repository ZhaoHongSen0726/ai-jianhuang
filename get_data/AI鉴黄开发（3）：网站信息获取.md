# 前言
进入新的部分了，这个阶段的主要任务就是通过用户的信息来获取到网站，然后对其网站进行信息的爬取。但是吧，这里有个很大的问题就是我无法获取到如此大量的数据集让我去训练呀，网上的鉴黄数据集其实也是有的，但是好像他们都是基于图像的，我想做个基于文本的好像没有呀
# 问题：数据集匮乏
怎么办？怎么去解决数据集不够的问题，就是工程中也是，如果数据集不够怎么办？那就想办法去收集到数据集

问题解决了，在大家共同的努力下，找到了很多的数据网站。。。对就是这样，
# 开始爬取网站了
这里的话肯定是要用到爬虫技术，也就是去获取网站数据。
## requests库学习
首先我们就要进入官网，查看文档来学习了。
https://docs.python-requests.org/zh_CN/latest/

![在这里插入图片描述](https://img-blog.csdnimg.cn/8d28d6c8499b4c1b87369a7005a5f495.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA56We5L2R5oiR6LCD5Y-C5L6g,size_20,color_FFFFFF,t_70,g_se,x_16)

这里因为我是又重新建立了一个虚拟环境，本次开发我打算使用pytorch进行，因为我用过飞桨嘛，所以这回试试这个，然后我发现我的电脑里是有gpu的，gtx1060还是可以的，那我们来安装一下吧

```python
pip install requests
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/892e7d00020c452499af795e519fae2b.png)

然后我就可以开始快乐的学习了！只需要3行代码就可以得到数据了，我们访问的网站是静态网站：

```python
import requests

r = requests.get("https://baoava.com/vodplay/90732-1-1/")
print(r.text)
```
然后我们就可以看到获取的内容了：

![在这里插入图片描述](https://img-blog.csdnimg.cn/3cf6f31870274ac69f1e8cb24123970f.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA56We5L2R5oiR6LCD5Y-C5L6g,size_20,color_FFFFFF,t_70,g_se,x_16)

额，懂得都懂啊。我是没想到这个网站这么好爬。
## 写入数据
那下一件事就是将爬取到的数据放到txt文件中。这里面会用到一个bs4的库啊，然后我们先安装一下：

```python
pip3 install Beautifulsoup4 
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/2d8d07c6f38045638485b2547da60d49.png)

然后的话看一下这个库的文档：https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html

Beautiful Soup 是一个可以从HTML或XML文件中提取数据的Python库.使用的方法如下：

```python
import requests
from bs4 import BeautifulSoup

r = requests.get("https://baoava.com/vodplay/90732-1-1/")
#print(r.text)
f1 = open("data/sex/1.txt")
soup = BeautifulSoup(r.text)
print(soup.prettify())
```
通过上面的简单的代码，现在我们就可以看到标准格式的输出了：

![在这里插入图片描述](https://img-blog.csdnimg.cn/e44b1018eaf945009f5bc6a9e008f88b.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA56We5L2R5oiR6LCD5Y-C5L6g,size_20,color_FFFFFF,t_70,g_se,x_16)

然后也可以直接获得所有的文字内容，看看效果

```python
print(soup.get_txt()
```
这个api会返回字符串，但是我们要进行处理一下，就是将空格都去掉。

![在这里插入图片描述](https://img-blog.csdnimg.cn/d1f711ab110f4e7da95abaf4086a03b0.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA56We5L2R5oiR6LCD5Y-C5L6g,size_20,color_FFFFFF,t_70,g_se,x_16)

这里的话想使用replace，但是不知道为什么不可以！后面改用了split的方法，然后我们看下效果：

![在这里插入图片描述](https://img-blog.csdnimg.cn/62348cae14184fdca9ab92c607d1bdee.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA56We5L2R5oiR6LCD5Y-C5L6g,size_20,color_FFFFFF,t_70,g_se,x_16)

嘿嘿，成功了啊，现在可以批量采集数据集了，这里我想想用不用多线程呢，先用单线程实现一下，下一步找到网页间的联系，然后我们就可以遍历到全部的网站了，这里的话我打算弄个500个txt文件吧，然后我们弄5个黄色网站，就有2500个数据，然后正常的我们也弄2500个 ，最后一共5000个文本文件，到时候先跑一遍试试！

然后可以看下这个函数，可以返回去掉换行符的字符串
>Python strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。

然后我们看一下这一部分的代码吧，还是很简单的

```python
import requests
from bs4 import BeautifulSoup

r = requests.get("https://baoava.com/vodplay/90732-1-1/")
#print(r.text)
f1 = open("D:\\go\\AI鉴黄\\old_data\\sex\\1.txt","w",encoding="utf-8")
soup = BeautifulSoup(r.text)
a = soup.get_text().replace(" ","")
f1.write(a)
f1.close()

with open("D:\\go\\AI鉴黄\\old_data\\sex\\1.txt","r",encoding='utf-8') as f2,open("D:\\go\\AI鉴黄\\data\\sex\\1.txt","w",encoding='utf-8') as fd:
    a = f2.readlines()
    for i in a:
        if i.strip():
            fd.write(i)

print("done")
```
>这里有个细节就是读和写的文件不要是一个，否则会出问题
## 批量采集数据集
然后也是成功发现了规律，这个网页是真的简单，只是用改变网页标签就可以了。

我也是找到了规律，然后的话弄500个，就是10个类别，每个类别50个网站！我采用的方法可能是不那么太自动化吧，但是决定是很简单的，我通过构造网页的字符串来访问，话不多说开干！

```python
#构建网页
for i in range(1,11):
    for j in range(1,50):
        r = "https://baoava.com/vodplay/"+i+"-"+j+"/"
```
然后就开始爬取了
![在这里插入图片描述](https://img-blog.csdnimg.cn/39c6f1f474344fadb8bce459bf8a4d91.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA56We5L2R5oiR6LCD5Y-C5L6g,size_20,color_FFFFFF,t_70,g_se,x_16)

## 爬取第二个网站
爬取后就会出现乱码的问题了，后来发现要先指定爬取的网站的编码格式，之后才能访问：

```python
url = "https://www.2b33699ffb5f597c.com/shipin/list-%E4%BA%9A%E6%B4%B2%E7%94%B5%E5%BD%B1-2.html"
print(url)
r = requests.get(url)
r.encoding = "utf-8"
```
然后我就要开始爬取第二个网站了，我觉得爬4个就可以了，太多了自己就不太想弄了。
## 爬取第三个网站
前两个网站都是静态网页，但是这个是动态网页，即是通过JavaScript动态生成的，就是把源代码隐藏起来了，下面看一下：

![在这里插入图片描述](https://img-blog.csdnimg.cn/2a4ca245e1ea4b7fa59574dad1a3f3b4.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA56We5L2R5oiR6LCD5Y-C5L6g,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://img-blog.csdnimg.cn/b5921e3c56f048bf97337791c1ecaf32.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA56We5L2R5oiR6LCD5Y-C5L6g,size_20,color_FFFFFF,t_70,g_se,x_16)
可以清楚的就看到这两个是完全不一样的，这时处理起来就比静态网页麻烦的多了。

### 开始破解动态网页
这里我们要用到的技术就是逆向工程，而要使用的工具就是自动化测试工具selenium
### 自动化测试工具selenium
下面我们先进行安装：

```python
pip3 install selenium
```
安装成功！

![在这里插入图片描述](https://img-blog.csdnimg.cn/67c65fbd5337408cb753d6223e41919b.png)
### 安装依赖
对了，使用selenium去自动化操作浏览器的时候要下载个依赖，并且放到环境变量中！
下载地址：http://npm.taobao.org/mirrors/chromedriver/
可以借鉴下面这个博客，多的不说了，自己去看去
https://blog.csdn.net/weixin_44335092/article/details/109054128
然后运行代码就可以自动化操作浏览器了，嘿嘿！

![在这里插入图片描述](https://img-blog.csdnimg.cn/172f6193872a403dbff7f0cc75d7c68f.png)
然后也是实现出来了呀，我们来看看代码：

```python
# -*- coding:utf-8 -*-
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r"D:/chromedriver_win32/chromedriver.exe")

for j in range(1,51,1):
    url = "https://www.ab48d.com/pc/video?label_ids=5&page="+str(j)
    driver.get(url)
    driver.encoding = "utf-8"
    #对于动态网页的时候一定要做到延迟。
    time.sleep(5)
    #这里面后期得判断一下是静态网页还是动态网页
    soup = BeautifulSoup(driver.page_source)
    a = soup.get_text()

    old_txt = "../old_data/sex/" + "1" + "_" + str(j) + ".txt"
    new_txt = "../data/sex/" + "1" + "_" + str(j) + ".txt"
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
```
>然后的话说下这里面的几个细节:首先我们实例化个对象，这里我是直接指定文件路径的，然后其他也跟上面的差不多，但是要注意，一定延时，因为js渲染需要一定的时间，然后不要关闭dirver，会自己刷新。但就是每次都得等5秒，有点慢，但是也是解决掉动态网页的问题了，嘿嘿。
