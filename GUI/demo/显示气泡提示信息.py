import  sys
from PyQt5.QtWidgets import QWidget,QApplication,QToolTip
from PyQt5.QtGui import QFont

class Winform(QWidget):
    def __init__(self,parent = None):
        super(Winform,self).__init__(parent)
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont("SansSerif",20))
        self.setToolTip("这是一个<b>气泡提醒</b>")
        self.setGeometry(200,300,400,400)
        self.setWindowTitle("气泡提醒demo")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Winform()
    win.show()
    sys.exit(app.exec_())