import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QPixmap("images/rabbit.png")

    def paintEvent(self,e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0,0,0))
        p.setBrush(QColor(244, 66, 235))
        #p.drawPolygon([QPoint(70,100),QPoint(100,110),QPoint(130,100),QPoint(100,150),])

        p.setPen(QColor(239, 91, 69))
        p.setBrush(QColor(252, 83, 58))
        p.drawPie(50,150,100,100,0, 180*16)
        p.drawPie(150,150,100,100,0, 180*16)

        p.drawPolygon([QPoint(50,200),QPoint(250,200),QPoint(150,350),])

        p.drawPixmap(QRect(400,100,320,320),self.rabbit)
        p.end()

def main():
    app = QApplication(sys.argv)

    w = Simple_drawing_window()
    w.show()

    return app.exec_()

if __name__ == '__main__':
    sys.exit(main())
