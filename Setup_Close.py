# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\kaste\Desktop\Uni\AgentsAndInterfaces\CourseProject\Interface\Setup_Close.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Credits(object):
    def setupUi(self, Credits):
        Credits.setObjectName("Credits")
        Credits.resize(400, 200)
        Credits.setMinimumSize(QtCore.QSize(400, 200))
        Credits.setMaximumSize(QtCore.QSize(400, 200))
        self.label = QtWidgets.QLabel(Credits)
        self.label.setGeometry(QtCore.QRect(30, 10, 341, 101))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.closeBtn = QtWidgets.QPushButton(Credits)
        self.closeBtn.setGeometry(QtCore.QRect(150, 120, 93, 28))
        self.closeBtn.setObjectName("closeBtn")
        self.closeBtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.line = QtWidgets.QFrame(Credits)
        self.line.setGeometry(QtCore.QRect(10, 0, 20, 211))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Credits)
        self.line_2.setGeometry(QtCore.QRect(370, 0, 20, 211))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Credits)
        self.line_3.setGeometry(QtCore.QRect(0, 170, 401, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Credits)
        self.line_4.setGeometry(QtCore.QRect(0, 10, 401, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")

        self.retranslateUi(Credits)
        QtCore.QMetaObject.connectSlotsByName(Credits)

    def retranslateUi(self, Credits):
        _translate = QtCore.QCoreApplication.translate
        Credits.setWindowTitle(_translate("Credits", "Credits"))
        self.label.setText(_translate("Credits", "This was a small Interface Project by Kersten Benecke\n"
"Special Thanks to Kajetan for (as always) being a big help"))
        self.closeBtn.setText(_translate("Credits", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Credits = QtWidgets.QWidget()
    ui = Ui_Credits()
    ui.setupUi(Credits)
    Credits.show()
    sys.exit(app.exec_())

