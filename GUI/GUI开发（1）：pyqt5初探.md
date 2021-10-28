# GUI开发

这里的话我打算使用pyqt开发，不多说了，找本书来开始学习，我会将pdf放到gitee工程中的。

![在这里插入图片描述](https://img-blog.csdnimg.cn/b4a01e37720a4e3eb688e391f07083b3.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA56We5L2R5oiR6LCD5Y-C5L6g,size_20,color_FFFFFF,t_70,g_se,x_16)
# PyQt5学习
## 先进行安装
```python
pip3 install PyQt5 -i https://pypi.douban.com/simple
pip3 install PyQt5-tools -i https://pypi.douban.com/simple
```
安装下面那个是因为现在Qt Designer并不会在上面那个一起安装了。
然后再path中添加pyqt-tool的路径

![在这里插入图片描述](https://img-blog.csdnimg.cn/199abcd64b5747a69052972d72c504fa.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA56We5L2R5oiR6LCD5Y-C5L6g,size_18,color_FFFFFF,t_70,g_se,x_16)
现在我们来测试一下

![在这里插入图片描述](https://img-blog.csdnimg.cn/5b07ae9c8c4c40918d0198b7701ee257.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA56We5L2R5oiR6LCD5Y-C5L6g,size_20,color_FFFFFF,t_70,g_se,x_16)
可以看到这里出现了个窗口所以成功了，下面我会写一些总结，但是代码的话我都会放在工程中！
## 使用一下qt designer
![在这里插入图片描述](https://img-blog.csdnimg.cn/5672c13f31d34f56ad6a8c5aa35c427c.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA56We5L2R5oiR6LCD5Y-C5L6g,size_20,color_FFFFFF,t_70,g_se,x_16)
ctrl + R 来测试预览
但是这里我并不建议上来就用这些工具呀，我应该从底层开搭

---
## 基本窗口控件
### 创建主窗口
![在这里插入图片描述](https://img-blog.csdnimg.cn/4b68fafc2b484b59a3281d2b4ccc88f9.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/c845377da3224b9daeae2ee9fc589219.png)
前者就相当于主窗口，后者相当于对话窗口的基类，下面来写创建一个主窗口的代码：
这里面是有一个模板的，然后在这个模板上添加，我们一步步分析：

```python
#导入需要的库
import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon
```
* sys的话就是对标操作系统的模块
* 对于第二行的话就是QtWidgets是一个文件名，然后里面是很多的路径连接，后面两个是两个类，第一个就是主窗口吗，第二个作用比较特殊，并不是一个窗口的类，QApplication:管理GUI程序的控制流和主要设置。这个很强，如果想要做一个GUI的话，那么一定会有一个且只有一个这个QApplication，这个后期一边做一边学吧
* 然后说下第三个吧，简要说明就是添加图标的

然后看下主函数中的：

```python
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/cartoon1.ico"))
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())
```
首先第一步是创建一个QApplication实例化对象，参数是命令行参数，然后设置一下窗口图标，实例化一个主窗口对象，窗口展示，最后循环运行app。

```python
class MainWindow(QMainWindow):
    def __init__(self,parent = None):
        super(MainWindow, self).__init__((parent))
        self.resize(400,200)
        self.status = self.statusBar()
        self.status.showMessage("这是状态栏提示",5000)
        self.setWindowTitle("PyQt MainWindow例子")
```
最后看下这个类：继承QMainWindow，然后初始化这都是模板，定义属性：大小，实例化一个bar型状态栏的对象，展示5s信息，最后写一下标题，总体还是很简单的，下一个。

---

### 在屏幕中间显示主窗口
```python
from PyQt5.QtWidgets import QDesktopWidget,QApplication,QMainWindow
import sys

class Winform(QMainWindow):
    def __init__(self,parent=None):
        super(Winform, self).__init__(parent)
        self.setWindowTitle("主窗口局中显示")
        self.resize(648,480)
        self.center()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width())/2, (screen.height() - size.height())/2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    wiin = Winform()
    wiin.show()
    sys.exit(app.exec_())

```
主函数和继承的类差不多，说一下上面那个没有的吧：多导入了QDesktopWidget的库，这个主要是对屏幕信息的访问，然后说下这个center的方法，并不是说上来就在屏幕中间显示，而是先显示后移动到了屏幕中间，先说下我们的QMainWindow真的是有很多api呀，像这里面的.geometyr()是获取主窗口的窗口信息，然后move是移动窗口，还可以获取大小，screen是我们的屏幕的信息，然后和窗口信息运算就行了，下一个

---
### 关闭主窗口

```python
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget,QHBoxLayout,QPushButton
import sys

class Winform(QMainWindow):
    def __init__(self,parent=None):
        super(Winform,self).__init__()
        self.setWindowTitle("关闭主窗口案例")
        self.button1 = QPushButton("关闭主窗口")
        self.button1.clicked.connect(self.onButtonClick)

        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        main_frame = QWidget()
        main_frame.setLayout(layout)
        self.setCentralWidget(main_frame)

    def onButtonClick(self):
        sender = self.sender()
        print(sender.text() + "被按下了")
        qApp = QApplication.instance()
        qApp.quit()

if __name__ =="__main__":
    app = QApplication(sys.argv)
    form = Winform()
    form.show()
    sys.exit(app.exec_())
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/7b597c1f37694b788aa1707dd62ce4c2.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA56We5L2R5oiR6LCD5Y-C5L6g,size_12,color_FFFFFF,t_70,g_se,x_16)

![在这里插入图片描述](https://img-blog.csdnimg.cn/9651460f03e64310b0aac7b21b944c89.png)

这个例子中是有很多我们以前没有接触到的东西呀，我们一步步来看：
这里面多了几个库啊，我们来看看
* QPushButton：这个看名就能看出来是一个放置开关的库嘛
* QHBoxLayout：这个我是没讲过的，采用QHBoxLayout类，按照从左到右的顺序来添加控件，也就是说是一个控件布局管理的库呗
* QWidget：是基础控件，下一节会重点学习

然后主函数没什么说的，直接看类中的内容：直接从第8行开始，是先实例化了一个按钮对象，然后直接给了上面要显示的文字，然后这行代码就很重要了`self.button1.clicked.connect(self.onButtonClick)`，因为这是会涉及到一个响应，响应的内容就是下面定义的方法，即点击这个按钮后做出的反应。

然后的话是定义了一个QHBoxLayout对象，可以理解为画布吧，然后在上面放置一个开关，但是这时这个画布还没有在我们的窗口上，所以在定义一个基本控件的对象，然后设置为我们上面定义好的画布，最后将这个画布设置为中心窗口。

最后看一下这个方法吧：这里面的信号和槽在后面会具体学习，这里发送的就是按钮对象，我们通过text方法来获取，然后下面那个函数是返回应用程序对象，之后退出，继续学习


### QWidgt类
先看下窗口的坐标系统:

![在这里插入图片描述](https://img-blog.csdnimg.cn/876ef3ba46334030b233f685687c8edc.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA56We5L2R5oiR6LCD5Y-C5L6g,size_13,color_FFFFFF,t_70,g_se,x_16)

![在这里插入图片描述](https://img-blog.csdnimg.cn/71e7629cfe964b3398c1024822b3fe79.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA56We5L2R5oiR6LCD5Y-C5L6g,size_20,color_FFFFFF,t_70,g_se,x_16)

设置不可变动的窗口：

![在这里插入图片描述](https://img-blog.csdnimg.cn/29974e775ec54b57b6481be1f29d8d49.png)
### 显示QLabel标签
这个例子非常好，里面有很多内容，我后期做界面的时候都会用到，好好学习一下，先看看做出来的效果：

![在这里插入图片描述](https://img-blog.csdnimg.cn/2d179ad2799048808fd3ec42285fcc34.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA56We5L2R5oiR6LCD5Y-C5L6g,size_10,color_FFFFFF,t_70,g_se,x_16)

怎么样是不是特别想继续学下去，嘿嘿，那么开始吧：

```python
from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap,QPalette
import sys

class Window_demo(QWidget):
    def __init__(self):
        super().__init__()
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText("这是一个文本标签！")
        label1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window,Qt.blue)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<a href='#'>欢迎使用Python Gui应用</a>")

        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip("这是一个图片标签")
        label3.setPixmap(QPixmap("C:\\Users\\Administrator\\Pictures\\Saved Pictures\\1.jpg"))

        label4.setText("<A hrep='http://www.cnblogs.com/wangshuo1/'>欢迎访问信平的小屋</a>")
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip("这是一个超链接标签")

        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addStretch()
        vbox.addWidget(label2)
        vbox.addStretch()
        vbox.addWidget(label3)
        vbox.addStretch()
        vbox.addWidget(label4)

        label1.setOpenExternalLinks(True)
        label4.setOpenExternalLinks(False)
        label4.linkActivated.connect(link_clicked)

        label2.linkHovered.connect(link_hoverd)
        label1.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.setLayout(vbox)
        self.setWindowTitle("QLabel 例子")

def link_hoverd():
    print("点击label2")

def link_clicked():
    print("点击label4")

if __name__ =="__main__":
    app = QApplication(sys.argv)
    print(1)
    win = Window_demo()
    win.show()
    #sys.exit(app.exec_())
    app.exec_()
```
我们先看下导入的库：
1. QLabel：这个特别重要，QLabel用于显示文本或图像。没有提供用户交互功能。标签的外观可以通过各种方式进行配置，可以用于指定另一个小部件的焦点助记键。

![在这里插入图片描述](https://img-blog.csdnimg.cn/d0c61efe2c5c4feb80b5beba1d5470d7.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA56We5L2R5oiR6LCD5Y-C5L6g,size_16,color_FFFFFF,t_70,g_se,x_16)

2. QPalette：这个是管颜色的，然后有两个函数结合使用`     
		label1.setAutoFillBackground(True)

  		palette = QPalette()
  	    palette.setColor(QPalette.Window,Qt.blue)
  	    label1.setPalette(palette)`
先设置全背景，实例化个色板对象，设置颜色，放置到label上，效果：

![在这里插入图片描述](https://img-blog.csdnimg.cn/cb128630bd5746dfbfcf58a1056d1d08.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA56We5L2R5oiR6LCD5Y-C5L6g,size_13,color_FFFFFF,t_70,g_se,x_16)

这个主函数中没有什么东西，还是那些东西，然后我们具体看下那个类l吧：我们这个例子有4部分组成，所以需要创建4个label对象
>一般情况下，创建好窗口的话是setWindowText，便签的话是setText来附上文字，但如果是图片的话就不需要了，之后就会有放置位置的函数setAlignment，这个是父类的方法，所以都会用到，然后就是这些都设置好了后还要在添加实例化好的画布上，用 vbox.addWidget(label1)和  vbox.addStretch()组合，后者是占据空白地区的，最后放置画布并且显示

这里再说一下setToolTip这个函数，是一个提醒的标签，将鼠标放到窗口或者标签上一会就可以显示出来。

![在这里插入图片描述](https://img-blog.csdnimg.cn/d891e32ef95640239aaccefb3079f5a3.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA56We5L2R5oiR6LCD5Y-C5L6g,size_12,color_FFFFFF,t_70,g_se,x_16)

好下一个
### QLabel标签快捷键的使用
```python
from PyQt5.QtWidgets import *
import sys

class Qlabel_demo(QDialog):
    def __init__(self):
        super(Qlabel_demo, self).__init__()
        self.setWindowTitle("Qlabel例子")
        nameLb1 = QLabel('&name',self)
        nameEd1 = QLineEdit(self)
        nameLb1.setBuddy(nameEd1)

        nameLb2 = QLabel("&password",self)
        nameEd2 = QLineEdit(self)
        nameLb2.setBuddy(nameEd2)

        btn_ok = QPushButton('&ok')
        btn_cancel = QPushButton('&cancel')
        main_layout = QGridLayout(self)
        main_layout.addWidget(nameLb1,0,0)
        main_layout.addWidget(nameEd1,0,1,1,2)

        main_layout.addWidget(nameLb2,1,0)
        main_layout.addWidget(nameEd2,1,1,1,2)

        main_layout.addWidget(btn_ok,2,1)
        main_layout.addWidget(btn_cancel,2,2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    label_demo = Qlabel_demo()
    label_demo.show()
    sys.exit(app.exec_())

```
这个例子也是非常好的，有对话框了：

![在这里插入图片描述](https://img-blog.csdnimg.cn/a2ab107a92d6485181e650d25dcb82b3.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA56We5L2R5oiR6LCD5Y-C5L6g,size_9,color_FFFFFF,t_70,g_se,x_16)

然后我们说下吧：这回是另一个窗口了，我们也是第一次遇到，为对话框，但是也是和label结合使用的，这里有个细节，就是在设置标签名字的时候前面加上“&”就可以实现快速切换到该标签的功能，快捷键为alt+&后面的首字母，QLineEdit是创建文本框，就是name后面那个东西，然后setBuddy让两者结合起来，在创建两个按钮。

然后初探QT就到这里，我们现在开始开发页面，然后一边做一边学习！





















