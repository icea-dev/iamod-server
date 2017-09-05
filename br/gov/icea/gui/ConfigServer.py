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
import ConfigParser

import PySide
from PySide.QtCore import QRegExp
from PySide.QtGui import QMainWindow, QApplication, QMessageBox, QRegExpValidator, QIntValidator, QFileDialog, QLabel, QLineEdit

from wndMain import Ui_MainWindow

__version__ = '0.0.1'

__basePath__ = os.path.abspath(os.path.join(os.getcwd(), '../../../..'))
__packagePath__ = '/br/gov/icea/'

print "basePath: " + __basePath__

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        #Validators for data input
        ipRange = "(?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])"
        ipRegex = QRegExp("^" + ipRange
                 + "\\." + ipRange
                 + "\\." + ipRange
                 + "\\." + ipRange + "$")
        ipValidator = QRegExpValidator(self.leGraylogIP)
        ipValidator.setRegExp(ipRegex)

        self.leGraylogIP.setValidator(ipValidator)
        self.leGraylogPort.setValidator(QIntValidator(1, 65535))

        self.leAsterixIP.setValidator(ipValidator)
        self.leAsterixPort.setValidator(QIntValidator(1, 65535))

        #Define functions for GUI actions
        self.pbStart.clicked.connect(self.__startServer)
        self.pbStop.clicked.connect(self.__stopServer)
        self.actionLicense.triggered.connect(self.__license)
        self.actionLoad_Config_File.triggered.connect(self.__dialogConfigFile)

        self.tabWidget.currentChanged.connect(self.__tabSelection)

        self.pbSaveConfiguration.clicked.connect(self.__writeConfigFile)

        if self.__checkServerIsRunning():
            self.__serverStatusImage(True)
        else:
            self.__serverStatusImage(False)

        self.__tabSelection()

        self.configFile = ConfigParser.ConfigParser()

    def __dialogConfigFile(self):
        self.configFileName = QFileDialog.getOpenFileName()
        self.__loadConfigFile()


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

    def __tabSelection(self):
        if (self.tabWidget.currentIndex() == 1):
            self.__blockEditConfiguration(not self.__checkServerIsRunning())

    def __blockEditConfiguration(self, block):
        self.tabWidget.currentWidget().setEnabled(block)

    def __loadConfigFile(self):
        fileName = self.configFileName[0]
        if (os.path.exists(fileName)):
            self.configFile.read(fileName)
            self.__readFile()

    def __readFile(self):
        try:
            graylogIp = self.configFile.get("graylog", "server")
        except:
            graylogIp = ""
        try:
            graylogPort = self.configFile.get("graylog", "port")
        except:
            graylogPort = ""
        try:
            asterixIp = self.configFile.get("asterix", "server")
        except:
            asterixIp = ""
        try:
            asterixPort = self.configFile.get("asterix", "port")
        except:
            asterixPort = ""
        self.leGraylogIP.setText(graylogIp)
        self.leGraylogPort.setText(graylogPort)
        self.leAsterixIP.setText(asterixIp)
        self.leAsterixPort.setText(asterixPort)


    def __writeConfigFile(self):
        print "wrinting"
        asterixIp = self.leAsterixIP.text()
        asterixPort = self.leAsterixPort.text()
        print "IP: " + asterixIp + " port: " + asterixPort
        self.configFile.set("asterix","server",asterixIp)
        self.configFile.set("asterix", "port", asterixPort)
        self.configFile.write(self.configFile[0])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.show()
    app.exec_()
