from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from configparser import ConfigParser
from tkinter import messagebox
import requests
import os
import webbrowser

config = ConfigParser()
config.read('main/savedata/version.ini')

url = 'https://raw.github.com/marksh16/OSgame/main/version.txt'
page = requests.get(url)


current_version = config['DEFAULT']['version']
newest_version = page.text
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(823, 564)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.info = QtWidgets.QTextBrowser(self.centralwidget)
        self.info.setGeometry(QtCore.QRect(10, 0, 801, 471))
        self.info.setObjectName("info")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 470, 131, 20))
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 490, 131, 16))
        self.label_2.setObjectName("label_2")
        self.Update = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.update())
        self.Update.setGeometry(QtCore.QRect(10, 480, 93, 28))
        self.Update.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Update.setObjectName("Update")
        self.check = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.reload())
        self.check.setGeometry(QtCore.QRect(100, 480, 121, 28))
        self.check.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.check.setObjectName("check")
        self.launch = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.runapp())
        self.launch.setGeometry(QtCore.QRect(720, 480, 93, 28))
        self.launch.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.launch.setObjectName("launch")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 823, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def update(self):
        if int(current_version) != int(newest_version):
            update = QtWidgets.QErrorMessage()
            update.showMessage('This will redirect you to github.com. Updating is still in wip.')
            update.exec_()
            webbrowser.open('https://github.com/marksh16/OSgame-Download')
        else:
            no_update = QtWidgets.QErrorMessage()
            no_update.showMessage('No updates available')
            no_update.exec_()


    def reload(self):
        url == 'https://raw.github.com/marksh16/OSgame/main/version.txt'
        page == requests.get(url)
        self.label.update()
        self.label_2.update()

    def runapp(self):
        MainWindow.destroy()
        os.system('user.py')
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "OS_LAUNCHER"))
        self.info.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Thank you for downloading this game!</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Osgame</span><span style=\" font-family:\'arial,sans-serif\'; font-size:8pt; font-weight:696; color:#000000; background-color:#ffffff;\">©2021</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", f"Current Version: {current_version}"))
        self.label_2.setText(_translate("MainWindow", f"Newest Version: {newest_version}"))
        self.Update.setText(_translate("MainWindow", "Update"))
        self.check.setText(_translate("MainWindow", "Check for updates"))
        self.launch.setText(_translate("MainWindow", "Launch OS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
