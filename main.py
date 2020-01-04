from UI import Ui_MainWindow
import sqlite3
import sys
import sqlite3
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication)

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import (QMainWindow, QLabel, QLCDNumber, QMessageBox,
                             QCheckBox, QPlainTextEdit, QInputDialog,  QLineEdit, QTableWidget,
                             QTableWidgetItem, QSpinBox, QVBoxLayout, QColorDialog, QGridLayout)
from PyQt5.QtGui import QPainter, QBrush, QPen, QColor
from PyQt5.QtCore import Qt, pyqtSlot, QByteArray


from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
import random


class Example(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.move(200, 200)
        self.pushButton.setFixedSize(100, 100)
        self.objects = []
        self.pushButton.clicked.connect(self.new)
        self.setFixedSize(500, 500)

    def new(self):
        r = random.randrange(20, 200)
        x, y = random.randrange(0, 500), random.randrange(0, 500)
        r, g, b  = random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)
        self.objects.append([x, y, r, [r, g, b]])
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
        self.drawFlag(qp)
        qp.end()

    def drawFlag(self, qp):
        for i in self.objects:
            br =  QBrush(Qt.gray, Qt.SolidPattern)
            br.setColor(QColor(*i[3]));
            qp.setBrush(br)
            qp.drawEllipse(i[0], i[1], i[2], i[2])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
