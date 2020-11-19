import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QApplication


class ApplWindow(QDialog):
    def __init__(self):
        super(ApplWindow, self).__init__()
        self.ui = uic.loadUi('DemoLineEdit.ui', self)
        self.ui.btn_Hello.clicked.connect(self.Add)
        self.show()

    def Add(self):
        self.ui.lb_kq.setText(self.ui.lineEdit.text())
        self.ui.lb_kq.setText("hello " + self.ui.lineEdit.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ApplWindow()
    sys.exit(app.exec_())
