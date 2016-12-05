'''

    Pyazo is my final project for CS230 (Computing I)

    More info in the README

'''

#import all the things
import sys

sys.path.append('./modules')

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont, QCursor
from PyQt5.QtCore import Qt, QRect, QTimer

#Doing this the OOP way..
class Gui(QWidget):
    def __init__(self):

        self.__eventHandlers = []

    #Initialize the QApp/QWidget things
        super().__init__()

    #Add a default rectangle
        self.__rectangle = QRect(0, 0, 0, 0)
        self.__relativeX = 0
        self.__relativeY = 0

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
        self.setWindowFlags(Qt.FramelessWindowHint)
        #self.setAttribute(Qt.WA_NoSystemBackground, True)
        #self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowOpacity(.15)
        self.setAttribute(Qt.WA_PaintOnScreen)
    #Maximize the window
        self.showFullScreen()
    #Enable mouse tracking
        self.setMouseTracking(True)
    #Render the window
        self.show()

#Paint things
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
    #Paint the rectangle
        rectangleColor = QColor(0, 0, 0, 100)
        qp.setBrush(rectangleColor)
        qp.setPen(rectangleColor)
        qp.drawRect(self.__rectangle)
        qp.end()
#Handle the mouse events below
#press
    def mousePressEvent(self, event):
# 'Mouse Click'
    #update reactangle coords
        self.__rectangle.setCoords(event.x(), event.y(), event.x(), event.y())

        self.__relativeX = event.x()
        self.__relativeY = event.y()
    #repaint
        self.repaint()
#release
    def mouseReleaseEvent(self, event):
# 'Mouse Release'

    #Get the corners of our rectangle for use when actually taking the image from the screen
        x = self.__rectangle.left()
        y = self.__rectangle.top()

        width = self.__rectangle.width()
        height = self.__rectangle.height()

        self.__rectangle.setCoords(0, 0, 0, 0)
        self.update()
    #Hide the GUI after the button is released
        self.setVisible(False)
    #Fire our 'release' event, use the handler we defined, call it after we hide the GUI (so we don't get an image of the GUI)
    #Use a timer to create this effect, executing our handler in the QT event loop
    #also use a lambda function because singleShot requires anonymity
        QTimer.singleShot(0, lambda: self.__fire('release', x, y, width, height))
#drag
    def mouseMoveEvent(self, event):
        if(event.buttons() == Qt.LeftButton):
# 'Dragging'
        #update rectangle bottom left corner to the mouse pos
            if(event.x() > self.__relativeX):
                self.__rectangle.setRight(event.x())
                self.__rectangle.setLeft(self.__relativeX)
            elif(event.x() < self.__relativeX):
                self.__rectangle.setLeft(event.x())
                self.__rectangle.setRight(self.__relativeX)

            if(event.y() < self.__relativeY):
                self.__rectangle.setTop(event.y())
                self.__rectangle.setBottom(self.__relativeY)
            elif(event.y() > self.__relativeY):
                self.__rectangle.setBottom(event.y())
                self.__rectangle.setTop(self.__relativeY)
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
