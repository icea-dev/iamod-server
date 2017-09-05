# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wndMain.ui'
#
# Created: Mon Aug 28 16:55:15 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(538, 341)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabStatus = QtGui.QWidget()
        self.tabStatus.setObjectName("tabStatus")
        self.groupBox = QtGui.QGroupBox(self.tabStatus)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 125, 96))
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setStyleSheet("")
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pbStart = QtGui.QPushButton(self.groupBox)
        self.pbStart.setObjectName("pbStart")
        self.verticalLayout.addWidget(self.pbStart)
        self.pbStop = QtGui.QPushButton(self.groupBox)
        self.pbStop.setObjectName("pbStop")
        self.verticalLayout.addWidget(self.pbStop)
        self.groupBox_2 = QtGui.QGroupBox(self.tabStatus)
        self.groupBox_2.setGeometry(QtCore.QRect(180, 10, 101, 101))
        self.groupBox_2.setObjectName("groupBox_2")
        self.statusImage = QtGui.QLabel(self.groupBox_2)
        self.statusImage.setGeometry(QtCore.QRect(20, 20, 71, 81))
        self.statusImage.setText("")
        self.statusImage.setObjectName("statusImage")
        self.tabWidget.addTab(self.tabStatus, "")
        self.tabParameters = QtGui.QWidget()
        self.tabParameters.setObjectName("tabParameters")
        self.gbGraylog = QtGui.QGroupBox(self.tabParameters)
        self.gbGraylog.setEnabled(True)
        self.gbGraylog.setGeometry(QtCore.QRect(20, 10, 188, 96))
        self.gbGraylog.setObjectName("gbGraylog")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.gbGraylog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter = QtGui.QSplitter(self.gbGraylog)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label = QtGui.QLabel(self.splitter)
        self.label.setObjectName("label")
        self.leGraylogIP = QtGui.QLineEdit(self.splitter)
        self.leGraylogIP.setInputMask("")
        self.leGraylogIP.setObjectName("leGraylogIP")
        self.verticalLayout_2.addWidget(self.splitter)
        self.splitter_2 = QtGui.QSplitter(self.gbGraylog)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.label_2 = QtGui.QLabel(self.splitter_2)
        self.label_2.setObjectName("label_2")
        self.leGraylogPort = QtGui.QLineEdit(self.splitter_2)
        self.leGraylogPort.setInputMask("")
        self.leGraylogPort.setObjectName("leGraylogPort")
        self.verticalLayout_2.addWidget(self.splitter_2)
        self.gbAsterix = QtGui.QGroupBox(self.tabParameters)
        self.gbAsterix.setGeometry(QtCore.QRect(250, 20, 211, 96))
        self.gbAsterix.setObjectName("gbAsterix")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.gbAsterix)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.splitter_4 = QtGui.QSplitter(self.gbAsterix)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.label_3 = QtGui.QLabel(self.splitter_4)
        self.label_3.setObjectName("label_3")
        self.leAsterixIP = QtGui.QLineEdit(self.splitter_4)
        self.leAsterixIP.setObjectName("leAsterixIP")
        self.verticalLayout_3.addWidget(self.splitter_4)
        self.splitter_3 = QtGui.QSplitter(self.gbAsterix)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.label_4 = QtGui.QLabel(self.splitter_3)
        self.label_4.setObjectName("label_4")
        self.leAsterixPort = QtGui.QLineEdit(self.splitter_3)
        self.leAsterixPort.setObjectName("leAsterixPort")
        self.verticalLayout_3.addWidget(self.splitter_3)
        self.pbSaveConfiguration = QtGui.QPushButton(self.tabParameters)
        self.pbSaveConfiguration.setGeometry(QtCore.QRect(190, 200, 98, 27))
        self.pbSaveConfiguration.setObjectName("pbSaveConfiguration")
        self.tabWidget.addTab(self.tabParameters, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 538, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionLicense = QtGui.QAction(MainWindow)
        self.actionLicense.setObjectName("actionLicense")
        self.actionLoad_Config_File = QtGui.QAction(MainWindow)
        self.actionLoad_Config_File.setObjectName("actionLoad_Config_File")
        self.menuFile.addAction(self.actionLoad_Config_File)
        self.menuFile.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionLicense)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL("activated()"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "IAMOD Server", None, QtGui.QApplication.UnicodeUTF8))
        self.pbStart.setText(QtGui.QApplication.translate("MainWindow", "Start Server", None, QtGui.QApplication.UnicodeUTF8))
        self.pbStop.setText(QtGui.QApplication.translate("MainWindow", "Stop Server", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Server Status", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabStatus), QtGui.QApplication.translate("MainWindow", "Server Status", None, QtGui.QApplication.UnicodeUTF8))
        self.gbGraylog.setTitle(QtGui.QApplication.translate("MainWindow", "Graylog Configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "IP:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Port:", None, QtGui.QApplication.UnicodeUTF8))
        self.gbAsterix.setTitle(QtGui.QApplication.translate("MainWindow", "Asterix Server Configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "IP:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Port:", None, QtGui.QApplication.UnicodeUTF8))
        self.pbSaveConfiguration.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabParameters), QtGui.QApplication.translate("MainWindow", "Server Parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbout.setTitle(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLicense.setText(QtGui.QApplication.translate("MainWindow", "License", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_Config_File.setText(QtGui.QApplication.translate("MainWindow", "Load Config File", None, QtGui.QApplication.UnicodeUTF8))

