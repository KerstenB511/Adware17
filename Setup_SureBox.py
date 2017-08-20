# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\kaste\Desktop\Uni\AgentsAndInterfaces\CourseProject\Interface\Setup_SureBox.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from random import randint
from Setup_Fin import Ui_FinWindow
from Setup_Boy import Ui_Form
from PyQt5.QtMultimedia import QSound

class HoverButton(QtWidgets.QPushButton):
    mouseHover = QtCore.pyqtSignal(bool)

    def __init__(self, parent=None):
        QtWidgets.QPushButton.__init__(self, parent)
        self.setMouseTracking(True)

    def enterEvent(self, event):
        self.mouseHover.emit(True)

    def leaveEvent(self, event):
        self.mouseHover.emit(False)


class Ui_SureBox(object):

    def jumpWindow(self):
        pos1 = randint(50, 1500)
        pos2 = randint(50, 800)
        SB.setGeometry(pos1, pos2, 400, 200)
        self.sound.play()


    def Boy(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window, MSW)
        self.window.show()
        SB.destroy()

    def setupUi(self, SureBox, MSWnew):
        global SB, MSW
        MSW = MSWnew
        SB = SureBox
        SureBox.setObjectName("SureBox")
        SureBox.resize(400, 200)
        SureBox.setMinimumSize(QtCore.QSize(400, 200))
        SureBox.setMaximumSize(QtCore.QSize(400, 200))
        self.label = QtWidgets.QLabel(SureBox)
        self.label.setGeometry(QtCore.QRect(50, 0, 301, 121))
        self.label.setStyleSheet("font: bold 8pt \"MS Shell Dlg 2\";")
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.sound = QSound("error.wav")
        self.buttonYes = HoverButton(SureBox)
        self.buttonYes.setGeometry(QtCore.QRect(260, 150, 93, 28))
        self.buttonYes.setObjectName("buttonYes")


        self.buttonYes.mouseHover.connect(self.jumpWindow)
       # self.buttonYes. connect(self.jumpWindow)

        self.buttonCheckUp = QtWidgets.QPushButton(SureBox)
        self.buttonCheckUp.setGeometry(QtCore.QRect(30, 150, 191, 28))
        self.buttonCheckUp.setStyleSheet("font: bold 8pt \"MS Shell Dlg 2\";")
        self.buttonCheckUp.setObjectName("buttonCheckUp")
        #self.buttonCheckUp.clicked.connect(self.OpenFin)
        self.buttonCheckUp.clicked.connect(self.Boy)

        self.line = QtWidgets.QFrame(SureBox)
        self.line.setGeometry(QtCore.QRect(0, 120, 411, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(SureBox)
        QtCore.QMetaObject.connectSlotsByName(SureBox)

    def retranslateUi(self, SureBox):
        _translate = QtCore.QCoreApplication.translate
        SureBox.setWindowTitle(_translate("SureBox", "Are You Sure?"))
        self.label.setText(_translate("SureBox", "Are you really sure you want to continue without SilverWare® BrowserCheckUp?"))
        self.buttonYes.setText(_translate("SureBox", "Yes"))
        self.buttonCheckUp.setText(_translate("SureBox", "Install BrowserChekUp"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SureBox = QtWidgets.QWidget()
    ui = Ui_SureBox()
    ui.setupUi(SureBox)
    SureBox.show()
    sys.exit(app.exec_())

