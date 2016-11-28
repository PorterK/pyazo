'''

    Pyazo is my final project for CS230 (Computing I)

    More info in the README

'''

#import all the things
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont, QCursor
from PyQt5.QtCore import Qt, QRect

#Doing this the OOP way..
class Gui(QWidget):
    def __init__(self):

    #Initialize the QApp/QWidget things
        super().__init__()

    #Add a default rectangle
        self.rectangle = QRect(0, 0, 0, 0)

    #Build the window in a method to keep the init clean
        self.buildWindow()

#Build the window
    def buildWindow(self):

    #Set the window title even though it will not be seen
        self.setWindowTitle('Pyazo')
    #Make the window transparent
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
    #Maximize the window
        self.resize(1920, 1080)
    #Enable mouse tracking
        self.setMouseTracking(True)
    #Render the window
        self.show()

#Paint things
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
    #Paint the rectangle
        rectangleColor = QColor(200, 200, 200, 100)
        qp.setBrush(rectangleColor)
        qp.setPen(rectangleColor)
        qp.drawRect(self.rectangle)
        qp.end()
#Handle the mouse events below
#press
    def mousePressEvent(self, event):
# 'Mouse Click'
    #update reactangle coords
        self.rectangle.setCoords(event.x(), event.y(), event.x(), event.y())
    #repaint
        self.repaint()
#release
    def mouseReleaseEvent(self, event):
# 'Mouse Release'
        self.setVisible(False)
#drag
    def mouseMoveEvent(self, event):
        if(event.buttons() == Qt.LeftButton):
# 'Dragging'
        #update rectangle bottom left corner to the mouse pos
            self.rectangle.setLeft(event.x())
            self.rectangle.setBottom(event.y())
        #repaint
            self.repaint()


#Main function
def main():
#Instantiate our app and Gui stuff.
    app = QApplication(sys.argv)
    gui = Gui()
#Make the cursor the "cross cursor" for effect
    app.setOverrideCursor(QCursor(Qt.CrossCursor))
#Exit when our app exits
    sys.exit(app.exec_())

#That one thing that we write for funzies (not really, its important)
if(__name__ == '__main__'):
    main()
