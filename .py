# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Imageframe = QtWidgets.QFrame(self.centralwidget)
        self.Imageframe.setGeometry(QtCore.QRect(830, 180, 171, 141))
        self.Imageframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Imageframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Imageframe.setObjectName("Imageframe")
        self.Name = QtWidgets.QTextEdit(self.centralwidget)
        self.Name.setGeometry(QtCore.QRect(810, 380, 71, 31))
        self.Name.setFrameShape(QtWidgets.QFrame.VLine)
        self.Name.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.Name.setObjectName("Name")
        self.Dayofbirth = QtWidgets.QTextEdit(self.centralwidget)
        self.Dayofbirth.setGeometry(QtCore.QRect(810, 420, 111, 31))
        self.Dayofbirth.setFrameShape(QtWidgets.QFrame.HLine)
        self.Dayofbirth.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.Dayofbirth.setObjectName("Dayofbirth")
        self.inforCCCD = QtWidgets.QLabel(self.centralwidget)
        self.inforCCCD.setGeometry(QtCore.QRect(890, 340, 111, 31))
        self.inforCCCD.setText("")
        self.inforCCCD.setObjectName("inforCCCD")
        self.inforName = QtWidgets.QLabel(self.centralwidget)
        self.inforName.setGeometry(QtCore.QRect(890, 380, 111, 31))
        self.inforName.setText("")
        self.inforName.setObjectName("inforName")
        self.inforDoB = QtWidgets.QLabel(self.centralwidget)
        self.inforDoB.setGeometry(QtCore.QRect(930, 420, 91, 31))
        self.inforDoB.setText("")
        self.inforDoB.setObjectName("inforDoB")
        self.CCCD = QtWidgets.QTextEdit(self.centralwidget)
        self.CCCD.setGeometry(QtCore.QRect(810, 340, 71, 31))
        self.CCCD.setFrameShape(QtWidgets.QFrame.VLine)
        self.CCCD.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.CCCD.setObjectName("CCCD")
        self.logoclb = QtWidgets.QLabel(self.centralwidget)
        self.logoclb.setEnabled(True)
        self.logoclb.setGeometry(QtCore.QRect(930, 40, 71, 71))
        self.logoclb.setStyleSheet("image: url(:/logo2/Pictures/bkmaker.png);\n"
"")
        self.logoclb.setText("")
        self.logoclb.setObjectName("logoclb")
        self.labekhoa = QtWidgets.QLabel(self.centralwidget)
        self.labekhoa.setEnabled(True)
        self.labekhoa.setGeometry(QtCore.QRect(830, 32, 73, 81))
        self.labekhoa.setStyleSheet("\n"
"image: url(:/logokhoa/Pictures/khoadien.png);\n"
"")
        self.labekhoa.setText("")
        self.labekhoa.setObjectName("labekhoa")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(800, 0, 231, 601))
        self.label.setStyleSheet("background-image: url(:/backgroundorange/Pictures/background8.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-10, 0, 811, 601))
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_2.setLineWidth(3)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label.raise_()
        self.Imageframe.raise_()
        self.Name.raise_()
        self.Dayofbirth.raise_()
        self.inforCCCD.raise_()
        self.inforName.raise_()
        self.inforDoB.raise_()
        self.CCCD.raise_()
        self.logoclb.raise_()
        self.labekhoa.raise_()
        self.label_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Name.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">Name :</span></p></body></html>"))
        self.Dayofbirth.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">Day of birth :</span></p></body></html>"))
        self.CCCD.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">CCCD :</span></p></body></html>"))
import background_rc
import logoclb2_rc
import logoclb_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
