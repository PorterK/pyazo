from Gui import *
import sys
import tempfile
import uuid
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QCursor, QScreen

def run():
    global app
#Instantiate our app and Gui stuff.
    app = QApplication(sys.argv)
    gui = Gui()

    gui.on('release', doRelease)
#Make the cursor the "cross cursor" for effect
    app.setOverrideCursor(QCursor(Qt.CrossCursor))
#Exit when our app exits
    sys.exit(app.exec_())

def doRelease(x, y, width, height):

    global app

    screen = app.primaryScreen()

    print('''
    x: {}
    y: {}
    width: {}
    height: {}
    '''.format(x, y, width, height))

    saveTempImage(screen.grabWindow(1, x, y, width / 2, height / 2))

def saveTempImage(pixmap):
    with tempfile.TemporaryDirectory() as tmpdir:
    #Generate a random uuid (these will never collide)
        randomId = uuid.uuid1()

        pixmap.save('{}/{}.png'.format(tmpdir, randomId.hex), 'PNG')
        print('Saved to {}/{}.png!!'.format(tmpdir, randomId.hex))


run()
