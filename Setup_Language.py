# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\kaste\Desktop\Uni\AgentsAndInterfaces\CourseProject\Interface\Setup_Language.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Setup_Main import Ui_MainSetupWindow

class Ui_languageBox_2(object):

    def openMain(self):
        self.window = QtWidgets.QStackedWidget()
        self.ui = Ui_MainSetupWindow()
        self.ui.setupUi(self.window)
        languageBox_2.hide()
        self.window.show()

    def setupUi(self, languageBox_2):
        languageBox_2.setObjectName("languageBox_2")
        languageBox_2.resize(400, 200)
        languageBox_2.setMinimumSize(QtCore.QSize(400, 200))
        languageBox_2.setMaximumSize(QtCore.QSize(400, 200))
        self.horizontalLayoutWidget = QtWidgets.QWidget(languageBox_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(190, 150, 195, 30))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonCancel_1 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.buttonCancel_1.setObjectName("buttonCancel_1")
        self.buttonCancel_1.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.horizontalLayout.addWidget(self.buttonCancel_1)
        self.buttonOK_1 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.buttonOK_1.setObjectName("buttonOK_1")
        self.buttonOK_1.clicked.connect(self.openMain)


        self.horizontalLayout.addWidget(self.buttonOK_1)
        self.languageBox = QtWidgets.QComboBox(languageBox_2)
        self.languageBox.setGeometry(QtCore.QRect(70, 90, 311, 22))
        self.languageBox.setObjectName("languageBox")
        self.languageBox.addItem("")
        self.languageBox.addItem("")
        self.labelChooseLanguage = QtWidgets.QLabel(languageBox_2)
        self.labelChooseLanguage.setGeometry(QtCore.QRect(70, 10, 311, 61))
        self.labelChooseLanguage.setWordWrap(True)
        self.labelChooseLanguage.setObjectName("labelChooseLanguage")

        self.retranslateUi(languageBox_2)
        QtCore.QMetaObject.connectSlotsByName(languageBox_2)

    def retranslateUi(self, languageBox_2):
        _translate = QtCore.QCoreApplication.translate
        languageBox_2.setWindowTitle(_translate("languageBox_2", "Choose Setup Language"))
        self.buttonCancel_1.setText(_translate("languageBox_2", "Cancel"))
        self.buttonOK_1.setText(_translate("languageBox_2", "OK"))
        self.languageBox.setItemText(0, _translate("languageBox_2", "English"))
        self.languageBox.setItemText(1, _translate("languageBox_2", "nothing else here, sorry"))
        self.labelChooseLanguage.setText(_translate("languageBox_2", "Choose a language that should be used during the install process."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    languageBox_2 = QtWidgets.QWidget()
    ui = Ui_languageBox_2()
    ui.setupUi(languageBox_2)
    languageBox_2.show()
    sys.exit(app.exec_())

