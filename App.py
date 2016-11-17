from Gui import *
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QCursor

def run():
#Instantiate our app and Gui stuff.
    app = QApplication(sys.argv)
    gui = Gui()
#Make the cursor the "cross cursor" for effect
    app.setOverrideCursor(QCursor(Qt.CrossCursor))
#Exit when our app exits
    sys.exit(app.exec_())

run()
