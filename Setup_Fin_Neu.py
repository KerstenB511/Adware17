# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\kaste\Desktop\Uni\AgentsAndInterfaces\CourseProject\Interface\Setup_Fin_Neu.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FinWindow(object):
    def setupUi(self, FinWindow):
        FinWindow.setObjectName("FinWindow")
        FinWindow.resize(600, 400)
        FinWindow.setMinimumSize(QtCore.QSize(600, 400))
        FinWindow.setMaximumSize(QtCore.QSize(600, 400))
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(40, 100, 501, 91))
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.page)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(380, 350, 195, 30))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonCancel01 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.buttonCancel01.setObjectName("buttonCancel01")
        self.horizontalLayout.addWidget(self.buttonCancel01)
        self.buttonNext01 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.buttonNext01.setObjectName("buttonNext01")
        self.horizontalLayout.addWidget(self.buttonNext01)
        self.label_4 = QtWidgets.QLabel(self.page)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 241, 61))
        self.label_4.setStyleSheet("font: bold 10pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.page)
        self.pushButton.setGeometry(QtCore.QRect(450, 200, 93, 21))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.page)
        self.lineEdit.setGeometry(QtCore.QRect(40, 200, 401, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.line_3 = QtWidgets.QFrame(self.page)
        self.line_3.setGeometry(QtCore.QRect(0, 320, 611, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_8 = QtWidgets.QFrame(self.page)
        self.line_8.setGeometry(QtCore.QRect(0, 90, 601, 16))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        FinWindow.addWidget(self.page)
        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName("page1")
        self.label_3 = QtWidgets.QLabel(self.page1)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 521, 51))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.page1)
        self.label_5.setGeometry(QtCore.QRect(20, 10, 241, 61))
        self.label_5.setStyleSheet("font: bold 10pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.line_7 = QtWidgets.QFrame(self.page1)
        self.line_7.setGeometry(QtCore.QRect(0, 90, 601, 16))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.progressBar = QtWidgets.QProgressBar(self.page1)
        self.progressBar.setGeometry(QtCore.QRect(20, 120, 541, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_2 = QtWidgets.QLabel(self.page1)
        self.label_2.setGeometry(QtCore.QRect(30, 140, 421, 131))
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.page1)
        self.pushButton_2.setGeometry(QtCore.QRect(480, 350, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.line_4 = QtWidgets.QFrame(self.page1)
        self.line_4.setGeometry(QtCore.QRect(0, 320, 611, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        FinWindow.addWidget(self.page1)

        self.retranslateUi(FinWindow)
        FinWindow.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(FinWindow)

    def retranslateUi(self, FinWindow):
        _translate = QtCore.QCoreApplication.translate
        FinWindow.setWindowTitle(_translate("FinWindow", "StackedWidget"))
        self.label.setText(_translate("FinWindow", "Choose a destination in which you would like to install the\n"
"AwesomeSoft Free Video Converter.\n"
"\n"
"Click \'Browse\' to select a file path, click \'next\' to continue and install the programm"))
        self.buttonCancel01.setText(_translate("FinWindow", "Back"))
        self.buttonNext01.setText(_translate("FinWindow", "Next"))
        self.label_4.setText(_translate("FinWindow", "Finish the Setup"))
        self.pushButton.setText(_translate("FinWindow", "Browse"))
        self.label_3.setText(_translate("FinWindow", "Please wait while the AwesomeSoft Video Converter is being installed on your Computer."))
        self.label_5.setText(_translate("FinWindow", "Installing"))
        self.label_2.setText(_translate("FinWindow", "Thank you for using the AwesomeSoft Free Video Converter."))
        self.pushButton_2.setText(_translate("FinWindow", "Finish"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FinWindow = QtWidgets.QStackedWidget()
    ui = Ui_FinWindow()
    ui.setupUi(FinWindow)
    FinWindow.show()
    sys.exit(app.exec_())

