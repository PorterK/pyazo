'''

    Pyazo is my final project for CS230 (Computing I)

    More info in the README

'''

#import all the things
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont, QCursor
from PyQt5.QtCore import Qt

#Doing this the OOP way..
class Gui(QWidget):
    def __init__(self):

    #Initialize the QApp/QWidget things
        super().__init__()

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
        self.showMaximized()
    #Render the window
        self.show()

#Handle the mouse events below

#press
    def mousePressEvent(self, event):
        print('mouse clicked!')
#release
    def mouseReleaseEvent(self, event):
        print('released!')


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
