import sys
from random import randint
from PyQt6.QtGui import QColor, QPainter
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 500, 500)
        self.btn = QPushButton('Magical button', self)
        self.btn.resize(100, 50)
        self.btn.clicked.connect(self.draw)
        self.do_draw = False

    def draw(self):
        self.do_draw = True
        self.update()

    def paintEvent(self, event):
        if self.do_draw:
            painter = QPainter()
            painter.begin(self)
            painter.setPen(QColor('yellow'))
            r = randint(10, 100)
            painter.drawEllipse(250, 250, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
