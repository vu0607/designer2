from cmath import log
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt5.QtGui import QPixmap
from designer import Ui_MainWindow
class MainWindow: #Setup Main Window
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        self.addimage() 
        self.showtext('10731283','DangNguyen','07/07/20','12B')
        self.addlogo()
        self.thread = {}
    def show(self):
        self.main_win.show()
    def addimage(self):  #Add image to Main Window
        qpixmap = QPixmap('/home/vudangitwork/Documents/t/pythonlogo.png')
        self.uic.image.setPixmap(qpixmap)
    def showtext(self,inforCCCD,inforName,inforDoB,inforClass):  #Add Text to Main Window
        self.uic.inforCCCD.setText(str(inforCCCD))
        self.uic.inforName.setText(str(inforName))
        self.uic.inforDoB.setText(str(inforDoB))
        self.uic.inforClass.setText(str(inforClass))
    def addlogo(self):  #Add logo and background
        logoclb = QPixmap('/home/vudangitwork/Documents/t/bkmaker.png')
        logokhoa = QPixmap('/home/vudangitwork/Documents/t/khoadien.png')
        background = QPixmap('/home/vudangitwork/Documents/t/background.png')
        self.uic.logoclb.setPixmap(logoclb)
        self.uic.logokhoa.setPixmap(logokhoa)
        self.uic.background.setPixmap(background)
if __name__ == "__main__": # Show Main Window
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())

