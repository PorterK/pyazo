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

        self.__eventHandlers = []

    #Initialize the QApp/QWidget things
        super().__init__()

    #Add a default rectangle
        self.rectangle = QRect(0, 0, 0, 0)

    #Build the window in a method to keep the init clean
        self.buildWindow()

#Custom event handling
    #Add events
    def on(self, eventName, handler):
        self.__eventHandlers.append([eventName, handler])

    #Fire events
    def __fire(self, eventName, *args):
        for event in self.__eventHandlers:
            if(event[0] == eventName):
                event[1](*args)


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

    #Get the corners of our rectangle for use when actually taking the image from the screen
        topRightCorner = (self.rectangle.right(), self.rectangle.top())
        topLeftCorner = (self.rectangle.left(), self.rectangle.top())

        bottomRightCorner = (self.rectangle.right(), self.rectangle.bottom())
        bottomLeftCorner = (self.rectangle.left(), self.rectangle.bottom())
    #Hide the GUI after the button is released
        self.setVisible(False)
    #Fire our 'release' event, use the handler we defined, call it after we hide the GUI (so we don't get an image of the GUI)
        self.__fire('release', topLeftCorner, topRightCorner, bottomRightCorner, bottomLeftCorner)
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
