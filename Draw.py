import PySide2
from PySide2.QtGui import QCursor, QPen, QColor,QBrush
from PySide2.QtWidgets import QGraphicsScene

class Draw(QGraphicsScene):
    def __init__(self):
        super(Draw, self).__init__()
        self.color = [0,0,0]

    def mouseMoveEvent(self, event:PySide2.QtWidgets.QGraphicsSceneMouseEvent):
        p = self.addEllipse(QCursor.pos().x(), QCursor.pos().y(), 20,20, QPen(QColor(self.color[0], self.color[1], self.color[2])),
                            QBrush(QColor(self.color[0], self.color[1], self.color[2])))
