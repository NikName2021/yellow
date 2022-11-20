import random
import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('yellow.ui', self)
        self.pushButton.clicked.connect(self.main)
        self.do_paint = False
        self.center = 0, 0
        self.shape = None
        self.setMouseTracking(True)

    def main(self):
        self.do_paint = True
        self.update()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def draw(self, qp):
        # qp.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        qp.setBrush(QColor(255, 239, 0))
        size = random.randint(100, 300)
        qp.drawEllipse(100, 100,
                       size, size)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())