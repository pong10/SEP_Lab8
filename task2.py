import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from Draw import Draw
from Ui_Form import Ui_Form

class Paint(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.setWindowTitle("Paint")

        self.g_view = self.ui.drawField

        self.g_sense = Draw()
        self.g_sense.setSceneRect(self.g_view.sceneRect())
        
        self.g_view.setScene(self.g_sense)
        
        self.setMouseTracking(True)
        
        self.ui.clear.clicked.connect(self.clearField)
        
    def clearField(self):
        print("Clear")
        self.g_sense.clear()
        
if __name__=='__main__':
    app = QApplication(sys.argv)
    w = Paint()
    w.show()
    sys.exit(app.exec_())
