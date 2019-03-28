import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import*
from PySide2.QtGui import*

class draw_star(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple drawing")
        self.rabbit = QPixmap("images/rabbit.png")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        p.setPen(QColor(65,105,225))
        p.setBrush(QColor(65,105,225))
        #p.drawPolygon([QPoint(0,85), QPoint(75,75), QPoint(100,10),QPoint(125,75), QPoint(200,85),
        #               QPoint(150,125),QPoint(160,190), QPoint(100,150), QPoint(40,190),QPoint(50,125), QPoint(0,85),])
        p.drawPolygon([QPoint(100, 50), QPoint(50, 150), QPoint(150, 150), ])
        p.drawPixmap(QRect(200,100,320,320), self.rabbit)
        p.end()



def main():
    app = QApplication(sys.argv)

    w = draw_star()
    w.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())