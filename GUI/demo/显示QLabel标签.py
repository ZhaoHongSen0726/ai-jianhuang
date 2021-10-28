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

        label4.setText("<A href='http://www.cnblogs.com/wangshuo1/'>欢迎访问信平的小屋</a>")
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