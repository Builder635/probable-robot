import sys
import math
import random
from PyQt6.QtCore import Qt, QRectF, QPointF
from PyQt6.QtGui import QPainter, QColor, QPolygonF
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton


class YellowCircle(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.update()
        self.setGeometry(100, 100, 1000, 1000)
        self.btn = QPushButton('Нарисовать круг', self)
        self.btn.move(400, 800)
        self.btn.resize(200, 30)
        self.btn.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_sq(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_sq(self, qp):
        side = random.randint(10, 500)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(QPointF(500, 500), side, side)