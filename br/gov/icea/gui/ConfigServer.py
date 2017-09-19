import sys
import subprocess
import platform
import os
import ConfigParser

import PySide
from PySide.QtCore import QRegExp, QUrl
from PySide.QtGui import QMainWindow, QApplication, QMessageBox, QRegExpValidator, QIntValidator, QFileDialog
from PySide.QtWebKit import QWebView, QWebSettings

from wndMain import Ui_MainWindow

__version__ = '0.1.0'

__basePath__ = os.path.abspath(os.path.join(os.getcwd(), '../../../..'))
__packagePath__ = '/br/gov/icea/'

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
        self.leGraylogHttpPort.setValidator(QIntValidator(1, 65535))

        ipValidator = QRegExpValidator(self.leAsterixIP)
        ipValidator.setRegExp(ipRegex)
        self.leAsterixIP.setValidator(ipValidator)
        self.leAsterixPort.setValidator(QIntValidator(1, 65535))
        self.leAsterixSic.setValidator(QIntValidator(1, 256))

        self.leIamodPort.setValidator(QIntValidator(1, 65535))
        self.leIamodThreshold.setValidator(QIntValidator(0, 99999))

        transponderRange = "(?:[0-7]?[0-7]?[0-7]?[0-7])"
        transponderRegex = QRegExp("^" + transponderRange)
        transponderValidator = QRegExpValidator(self.leIamodTransponder)
        transponderValidator.setRegExp(transponderRegex)
        self.leIamodTransponder.setValidator(transponderValidator)

        #Define functions for GUI actions
        self.pbStart.clicked.connect(self.__startServer)
        self.pbStop.clicked.connect(self.__stopServer)
        self.actionLicense.triggered.connect(self.__license)
        self.actionLoad_Config_File.triggered.connect(self.__dialogConfigFile)

        self.pbSaveConfiguration.clicked.connect(self.__writeConfigFile)
        self.pbStart.setEnabled(False)

        if self.__checkServerIsRunning():
            self.__serverStatusImage(True)
        else:
            self.__serverStatusImage(False)

        self.configFile = ConfigParser.ConfigParser()

        self.view = QWebView()
        self.webLayout.addWidget(self.view)

        self.view.settings().setAttribute(QWebSettings.JavascriptCanOpenWindows, True)
        self.view.settings().setAttribute(QWebSettings.LocalStorageEnabled, True)

        self.pbConnect.clicked.connect(self.__connectHttpServer)

    def __connectHttpServer(self):
        retCode = True
        retCode &= not self.leGraylogIP.text()
        retCode &= not self.leGraylogPort.text()
        print "Teste: " + str(retCode)
        if (not retCode):
            self.view.load(QUrl("http://" + self.leGraylogIP.text() + ":" + self.leGraylogHttpPort.text() + "/dashboards/599327b2b199cf24b0850bed"))
            self.view.show()
        else:
            QMessageBox.warning(self, "Error", "Please, fill Graylog IP and Http Port before connect!", QMessageBox.Ok)

    def __dialogConfigFile(self):
        self.configFileName = QFileDialog.getOpenFileName()
        self.__loadConfigFile()

    def __startServer(self):
        self.__serverStartStop('START')

    def __stopServer(self):
        self.__serverStartStop('STOP')
        self.pbStart.setEnabled(False)

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
                print "teste: " + scriptPath + "startServer.sh %s %s" %(str(iamodModule), str(self.configFileName[0]))
                subprocess.Popen(scriptPath + "startServer.sh %s %s" %(str(iamodModule), str(self.configFileName[0])), shell=True)
                self.statusbar.showMessage("Start IAMOD Server")
                self.__serverStatusImage(True)
            self.__blockEditConfiguration(False)
        else:
            subprocess.Popen(scriptPath + "stopServer.sh", shell=True)
            self.statusbar.showMessage("Stop IAMOD Server")
            self.__serverStatusImage(False)
            self.__blockEditConfiguration(True)

    def __serverStatusImage(self, image):
        if image == True:
            self.statusImage.setPixmap(__basePath__ + __packagePath__ + '/gui/icons/serverOn.png')
        else:
            self.statusImage.setPixmap(__basePath__ + __packagePath__ + '/gui/icons/serverOff.png')

    def __blockEditConfiguration(self, block):
        self.gbConfiguration.setEnabled(block)

    def __loadConfigFile(self):
        fileName = self.configFileName[0]
        if (os.path.exists(fileName)):
            self.configFile.read(fileName)
            self.__readFile()
            self.pbStart.setEnabled(True)

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
            graylogHttpPort = self.configFile.get("graylog", "httpPort")
        except:
            graylogHttpPort = ""
        try:
            asterixIp = self.configFile.get("asterix", "server")
        except:
            asterixIp = ""
        try:
            asterixPort = self.configFile.get("asterix", "port")
        except:
            asterixPort = ""
        try:
            asterixSic = self.configFile.get("asterix", "sic")
        except:
            asterixSic = ""
        try:
            iamodTranponderCode = self.configFile.get("iamod", "transponder")
        except:
            iamodTranponderCode = ""
        try:
            iamodPort = self.configFile.get("iamod", "port")
        except:
            iamodPort = ""
        try:
            iamodThreshold = self.configFile.get("iamod", "threshold")
        except:
            iamodThreshold = ""

        self.leGraylogIP.setText(graylogIp)
        self.leGraylogPort.setText(graylogPort)
        self.leGraylogHttpPort.setText(graylogHttpPort)

        self.leAsterixIP.setText(asterixIp)
        self.leAsterixPort.setText(asterixPort)
        self.leAsterixSic.setText(asterixSic)

        self.leIamodTransponder.setText(iamodTranponderCode)
        self.leIamodPort.setText(iamodPort)
        self.leIamodThreshold.setText(iamodThreshold)

    def __writeConfigFile(self):
        try:
            fileName = self.configFileName[0]
        except:
            fileName = ""
        if (not os.path.exists(fileName)):
            if (self.__validateForm()):
                self.configFileName = QFileDialog.getSaveFileName()
            else:
                QMessageBox.warning(self, "Error", "Please, fill all form before save!", QMessageBox.Ok)
                return

        cfgFile = open(self.configFileName[0], 'w')

        asterixIp = self.leAsterixIP.text()
        asterixPort = self.leAsterixPort.text()
        asterixSic = self.leAsterixSic.text()

        graylogIp = self.leGraylogIP.text()
        graylogPort = self.leGraylogPort.text()
        graylogHttpPort = self.leGraylogHttpPort.text()

        iamodTranponderCode = self.leIamodTransponder.text()
        iamodPort = self.leIamodPort.text()
        iamodThreshold = self.leIamodThreshold.text()

        self.configFile.set("asterix","server",asterixIp)
        self.configFile.set("asterix", "port", asterixPort)
        self.configFile.set("asterix", "sic", asterixSic)

        self.configFile.set("graylog", "server", graylogIp)
        self.configFile.set("graylog", "port", graylogPort)
        self.configFile.set("graylog", "httpPort", graylogHttpPort)

        self.configFile.set("iamod", "transponder", iamodTranponderCode)
        self.configFile.set("iamod", "port", iamodPort)
        self.configFile.set("iamod", "threshold", iamodThreshold)

        self.configFile.write(cfgFile)

    def __validateForm(self):
        retCode = True
        retCode &= not self.leIamodThreshold.text()
        retCode &= not self.leIamodTransponder.text()
        retCode &= not self.leIamodPort.text()
        retCode &= not self.leAsterixIP.text()
        retCode &= not self.leAsterixPort.text()
        retCode &= not self.leAsterixSic.text()
        retCode &= not self.leGraylogIP.text()
        retCode &= not self.leGraylogPort.text()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.showMaximized()
    app.exec_()
