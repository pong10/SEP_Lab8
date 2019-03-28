import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import*
from PySide2.QtGui import*

class Simple_drawing_window(QWidget):
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

        #Pong
        p.setPen(QColor(239, 91, 69))
        p.setBrush(QColor(252, 83, 58))
        p.drawPie(50, 150, 100, 100, 0, 180 * 16)
        p.drawPie(150, 150, 100, 100, 0, 180 * 16)

        p.drawPolygon([QPoint(50, 200), QPoint(250, 200), QPoint(150, 350), ])

        p.drawPixmap(QRect(200,100,320,320), self.rabbit)
        p.end()



def main():
    app = QApplication(sys.argv)

    w = Simple_drawing_window()
    w.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())