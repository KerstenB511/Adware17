# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\kaste\Desktop\Uni\AgentsAndInterfaces\CourseProject\Interface\Setup_Boy.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Setup_Fin import Ui_FinWindow

class Ui_Form(object):


    def OpenFin(self):
        self.window = QtWidgets.QStackedWidget()
        self.ui = Ui_FinWindow()
        self.ui.setupUi(self.window, MSW)
        MSW.hide()
        self.window.show()
        Fo.destroy()

    def setupUi(self, Form, MSWnew):
        global Fo, MSW
        Fo = Form
        MSW = MSWnew
        Form.setObjectName("Form")
        Form.resize(300, 100)
        Form.setMinimumSize(QtCore.QSize(300, 100))
        Form.setMaximumSize(QtCore.QSize(300, 100))
        self.goodBoyLabel = QtWidgets.QLabel(Form)
        self.goodBoyLabel.setGeometry(QtCore.QRect(110, 10, 71, 41))
        self.goodBoyLabel.setObjectName("goodBoyLabel")
        self.okButton = QtWidgets.QPushButton(Form)
        self.okButton.setGeometry(QtCore.QRect(100, 50, 93, 28))
        self.okButton.setObjectName("okButton")
        self.okButton.clicked.connect(self.OpenFin)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Finally"))
        self.goodBoyLabel.setText(_translate("Form", "Good Boy..."))
        self.okButton.setText(_translate("Form", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

