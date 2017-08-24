# Import PySide classes
# import sys
# from PySide.QtCore import *
# from PySide.QtGui import *
#
# # Create a Qt application
# app = QApplication(sys.argv)
# # Create a Label and show it
# label = QLabel("Hello World")
# label.show()
# # Enter Qt application main loop
# app.exec_()
# sys.exit()

import sys
import subprocess
import platform
import os
import PySide

from PyQt4.QtGui import QMessageBox
from PySide.QtGui import QMainWindow, QApplication, QMessageBox, QLabel

from wndMain import Ui_MainWindow

__version__ = '0.0.1'

__basePath__ = os.path.abspath(os.path.join(os.getcwd(), '../../../..'))
__packagePath__ = '/br/gov/icea/'

print "basePath: " + __basePath__

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        #Define functions for GUI actions
        self.pbStart.clicked.connect(self.__startServer)
        self.pbStop.clicked.connect(self.__stopServer)
        self.actionLicense.triggered.connect(self.__license)

        if self.__checkServerIsRunning():
            self.__serverStatusImage(True)
        else:
            self.__serverStatusImage(False)

    def __startServer(self):
        self.__serverStartStop('START')

    def __stopServer(self):
        self.__serverStartStop('STOP')

    def __license(self):
         '''Popup a box with about message.'''
         QMessageBox.about(self, "About PySide, Platform and the like",
         """<b>IAMOD Server GUI</b> {}
         
        <p>Copyright 2016, ICEA.
        <p>This file is part of atn-sim.
        <p>atn-sim is free software: you can redistribute it and/or modify
        it under the terms of the GNU General Public License as published by
        the Free Software Foundation, either version 3 of the License, or
        (at your option) any later version.

        <p>atn-sim is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU General Public License for more details.

        <p>You should have received a copy of the GNU General Public License
        along with this program.  If not, see <http://www.gnu.org/licenses/>.

        <p>Python {} - PySide version {} - Qt version {} on {}""".format(__version__,
        platform.python_version(), PySide.__version__, PySide.QtCore.__version__,
        platform.system()))

    def __checkServerIsRunning(self):
        p = subprocess.Popen(["ps", "-aux"], stdout=subprocess.PIPE)
        out, err = p.communicate()
        if ('iamod_server' in out):
            return True
        else:
            return False

    def __serverStartStop(self, mode):
        scriptPath = __basePath__ + __packagePath__ + 'scripts/'
        iamodModule = 'br.gov.icea.server.iamod_server'

        print "image: " + __basePath__ + __packagePath__ + '/gui/icons/serverOn.png'

        if (mode == 'START'):
            if self.__checkServerIsRunning():
                self.statusbar.showMessage("IAMOD Server is running")
            else:
                subprocess.Popen(scriptPath + "startServer.sh %s" %(str(iamodModule)), shell=True)
                self.statusbar.showMessage("Start IAMOD Server")
                self.__serverStatusImage(True)

        else:
            subprocess.Popen(scriptPath + "stopServer.sh", shell=True)
            self.statusbar.showMessage("Stop IAMOD Server")
            self.__serverStatusImage(False)

    def __serverStatusImage(self, image):
        if image == True:
            self.statusImage.setPixmap(__basePath__ + __packagePath__ + '/gui/icons/serverOn.png')
        else:
            self.statusImage.setPixmap(__basePath__ + __packagePath__ + '/gui/icons/serverOff.png')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.show()
    app.exec_()
