import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont, QCursor
from PyQt5.QtCore import Qt

class Gui(QWidget):
    def __init__(self):

        super().__init__()

        self.buildWindow()
        # self.addCanvas()

    def buildWindow(self):
        self.setWindowTitle('Icon')


        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.showMaximized()

        self.show()

    def mousePressEvent(self, event):
        print('mouse clicked!')

    def mouseReleaseEvent(self, event):
        print('released!')



def main():

    app = QApplication(sys.argv)
    gui = Gui()

    app.setOverrideCursor(QCursor(Qt.CrossCursor))

    sys.exit(app.exec_())

if(__name__ == '__main__'):
    main()
