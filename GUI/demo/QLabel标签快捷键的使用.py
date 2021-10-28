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
