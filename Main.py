import sys
from Stacked_DesignUI1 import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox, QGraphicsDropShadowEffect,QMessageBox
)
from PyQt5.QtCore import QPropertyAnimation
from PyQt5.QtGui import (QColor)

class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        QMainWindow.__init__(self)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("black"))
        self.ui.LeftMenu.setGraphicsEffect(self.shadow)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("black"))
        self.ui.Input_Widget.setGraphicsEffect(self.shadow)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("black"))
        self.ui.HeaderFrame_3.setGraphicsEffect(self.shadow)

        self.ui.btnUpdateStock.clicked.connect(lambda: self.OpenUpdatePage())
        self.ui.btnBuyStock.clicked.connect(lambda: self.OpenBuyStockPage())
        self.ui.btn_Report_Cost.clicked.connect(lambda: self.OpenReportCostPage())
        self.ui.menuBtn_2.clicked.connect(lambda: self.slideLeftMenu())
        self.show()
    def OpenBuyStockPage(self):
        self.ui.mainBody.setCurrentIndex(0)
    def OpenUpdatePage(self):
        self.ui.mainBody.setCurrentIndex(1)
    def OpenReportCostPage(self):
        self.ui.mainBody.setCurrentIndex(2)
    def slideLeftMenu(self):
        width=self.ui.frame_8.width()
        if(width==0):
            newWidth=200
            self.ui.menuBtn.setIcon(QtGui.QIcon(u":/blackicons/Graphics/featherBlack/chevron-left.svg"))
        else:
            newWidth=0
            self.ui.menuBtn.setIcon(QtGui.QIcon(u":/blackicons/Graphics/featherBlack/align-left.svg"))
        self.animation = QPropertyAnimation(self.ui.frame_8, b"maximumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)#Start value is the current menu width
        self.animation.setEndValue(newWidth)#end value is the new menu width
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

if __name__=="__main__":
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())