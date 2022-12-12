# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(600, 599)
        LoginWindow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        LoginWindow.setStyleSheet("#loginStackedWidgetPage1{\n"
"background-image:url(:/reset/Graphics/Login/output-onlinepngtools.png);\n"
"padding:10px 70px 15px 70px;\n"
"}\n"
"#emailinp{\n"
"height:25px;\n"
"margin-top:10px;\n"
"border:2px solid black;\n"
"border-radius : 6px;\n"
"padding:5px 15px;\n"
"}\n"
"#passwordinp{\n"
"height:25px;\n"
"margin-top:10px;\n"
"border:2px solid black;\n"
"border-radius : 6px;\n"
"padding:5px 15px;\n"
"}\n"
"#emailinp:hover,#passwordinp:hover{\n"
"border:2px solid gray;\n"
"}\n"
"\n"
"#emailinp:focus{\n"
"border:2px solid blue;\n"
"}\n"
"#passwordinp:focus{\n"
"border:2px solid blue;\n"
"}\n"
"#loginbtn{\n"
"margin-top:15px;\n"
"height:25px;\n"
"width:50px;\n"
"color:black;\n"
"background-color:qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0 rgba(20,47,78,20),stop:1 rgba(85,98,112,250));\n"
"border-radius:5px;\n"
"}\n"
"#loginbtn:pressed {\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(112,112,112,255);\n"
"    border-postion:calc(100% -10px)center;\n"
"}\n"
"#loginbtn:hover {\n"
"    background-color:rgba(112,112,112,255);\n"
"}\n"
"#forgotbtn{\n"
"margin-top:5px;\n"
"height:20px;\n"
"color:black;\n"
"border-radius:0px;\n"
"}\n"
"#forgotbtn:pressed {\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgb(255, 0, 0);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.loginStackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.loginStackedWidget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loginStackedWidget.setStyleSheet("")
        self.loginStackedWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.loginStackedWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.loginStackedWidget.setObjectName("loginStackedWidget")
        self.loginStackedWidgetPage1 = QtWidgets.QWidget()
        self.loginStackedWidgetPage1.setObjectName("loginStackedWidgetPage1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.loginStackedWidgetPage1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_5 = QtWidgets.QWidget(self.loginStackedWidgetPage1)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.widget_5)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/Login/Graphics/Login/ARM_LOGO_Crop-removebg-preview.png"))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.verticalLayout.addWidget(self.widget_5)
        self.loginimg = QtWidgets.QLabel(self.loginStackedWidgetPage1)
        self.loginimg.setText("")
        self.loginimg.setPixmap(QtGui.QPixmap(":/Login/Graphics/Login/user (2).png"))
        self.loginimg.setAlignment(QtCore.Qt.AlignCenter)
        self.loginimg.setObjectName("loginimg")
        self.verticalLayout.addWidget(self.loginimg)
        self.widget = QtWidgets.QWidget(self.loginStackedWidgetPage1)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.emailinp = QtWidgets.QLineEdit(self.widget)
        self.emailinp.setMinimumSize(QtCore.QSize(300, 0))
        self.emailinp.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.emailinp.setObjectName("emailinp")
        self.horizontalLayout.addWidget(self.emailinp)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.loginStackedWidgetPage1)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.passwordinp = QtWidgets.QLineEdit(self.widget_2)
        self.passwordinp.setMinimumSize(QtCore.QSize(300, 0))
        self.passwordinp.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordinp.setObjectName("passwordinp")
        self.horizontalLayout_2.addWidget(self.passwordinp)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.loginStackedWidgetPage1)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.forgotbtn = QtWidgets.QPushButton(self.widget_3)
        self.forgotbtn.setObjectName("forgotbtn")
        self.horizontalLayout_3.addWidget(self.forgotbtn)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.loginStackedWidgetPage1)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.loginbtn = QtWidgets.QPushButton(self.widget_4)
        self.loginbtn.setMinimumSize(QtCore.QSize(150, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Login/icons8-enter-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.loginbtn.setIcon(icon)
        self.loginbtn.setObjectName("loginbtn")
        self.horizontalLayout_4.addWidget(self.loginbtn)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.verticalLayout.addWidget(self.widget_4)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem9)
        self.loginStackedWidget.addWidget(self.loginStackedWidgetPage1)
        self.Reset1 = QtWidgets.QWidget()
        self.Reset1.setStyleSheet("#Reset1{\n"
"background-image:url(:/reset/Graphics/Login/output-onlinepngtools.png)\n"
"}\n"
"#mainlbl{\n"
"height:25px;\n"
"margin-top:20px;\n"
"}\n"
"#maillbl{\n"
"height:25px;\n"
"margin-top:10px;\n"
"padding:5px 10px;\n"
"}\n"
"#emailtxt{\n"
"height:25px;\n"
"border:2px solid black;\n"
"border-radius : 6px;\n"
"padding:5px 10px;\n"
"}\n"
"#emailtxt:hover{\n"
"border:2px solid gray;\n"
"}\n"
"#emailtxt:focus{\n"
"border:2px solid gray;\n"
"}\n"
"#backbtn , #sendbtn{\n"
"margin-top:15px;\n"
"height:25px;\n"
"width:50px;\n"
"color:black;\n"
"background-color:qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0 rgba(20,47,78,20),stop:1 rgba(85,98,112,250));\n"
"border-radius:5px;\n"
"}\n"
"#backbtnbtn:pressed , #sendbtn:pressed {\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(112,112,112,255);\n"
"    border-postion:calc(100% -10px)center;\n"
"}\n"
"#backbtn:hover , sendbtn:hover {\n"
"    background-color:rgba(112,112,112,255);\n"
"}\n"
"")
        self.Reset1.setObjectName("Reset1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Reset1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_6 = QtWidgets.QWidget(self.Reset1)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.resetframe = QtWidgets.QFrame(self.widget_6)
        self.resetframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.resetframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.resetframe.setObjectName("resetframe")
        self.formLayout = QtWidgets.QFormLayout(self.resetframe)
        self.formLayout.setObjectName("formLayout")
        self.logolbl = QtWidgets.QLabel(self.resetframe)
        self.logolbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.logolbl.setObjectName("logolbl")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.logolbl)
        self.mainlbl = QtWidgets.QLabel(self.resetframe)
        self.mainlbl.setAlignment(QtCore.Qt.AlignCenter)
        self.mainlbl.setObjectName("mainlbl")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.mainlbl)
        self.widget_7 = QtWidgets.QWidget(self.resetframe)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem10 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem10)
        self.maillbl = QtWidgets.QLabel(self.widget_7)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.maillbl.setFont(font)
        self.maillbl.setObjectName("maillbl")
        self.horizontalLayout_6.addWidget(self.maillbl)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem11)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.widget_7)
        self.widget_8 = QtWidgets.QWidget(self.resetframe)
        self.widget_8.setMinimumSize(QtCore.QSize(300, 0))
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem12 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem12)
        self.emailtxt = QtWidgets.QLineEdit(self.widget_8)
        self.emailtxt.setMinimumSize(QtCore.QSize(300, 0))
        self.emailtxt.setObjectName("emailtxt")
        self.horizontalLayout_7.addWidget(self.emailtxt)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem13)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.widget_8)
        self.widget_9 = QtWidgets.QWidget(self.resetframe)
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem14 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem14)
        self.backbtn = QtWidgets.QPushButton(self.widget_9)
        self.backbtn.setMinimumSize(QtCore.QSize(100, 0))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/reset/Graphics/reser/icons8-back-arrow-30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backbtn.setIcon(icon1)
        self.backbtn.setObjectName("backbtn")
        self.horizontalLayout_8.addWidget(self.backbtn)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem15)
        self.sendbtn = QtWidgets.QPushButton(self.widget_9)
        self.sendbtn.setMinimumSize(QtCore.QSize(100, 0))
        self.sendbtn.setObjectName("sendbtn")
        self.horizontalLayout_8.addWidget(self.sendbtn)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem16)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.widget_9)
        self.verticalLayout_3.addWidget(self.resetframe)
        self.verticalLayout_2.addWidget(self.widget_6)
        self.loginStackedWidget.addWidget(self.Reset1)
        self.gridLayout.addWidget(self.loginStackedWidget, 0, 0, 1, 1)
        LoginWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(LoginWindow)
        self.statusbar.setObjectName("statusbar")
        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginWindow)
        self.loginStackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "MainWindow"))
        self.emailinp.setPlaceholderText(_translate("LoginWindow", "@gmail.com"))
        self.passwordinp.setPlaceholderText(_translate("LoginWindow", "Password"))
        self.forgotbtn.setText(_translate("LoginWindow", "Forgot your password?"))
        self.loginbtn.setText(_translate("LoginWindow", "login"))
        self.logolbl.setText(_translate("LoginWindow", "<html><head/><body><p><img src=\":/reset/Graphics/Login/ARM_LOGO_Crop-removebg-preview.png\"/></p></body></html>"))
        self.mainlbl.setText(_translate("LoginWindow", "<html><head/><body><p><img src=\":/reset/Graphics/reser/icons8-forgot-password-30.png\"/></p></body></html>"))
        self.maillbl.setText(_translate("LoginWindow", "Enter your email:"))
        self.backbtn.setText(_translate("LoginWindow", "Back"))
        self.sendbtn.setText(_translate("LoginWindow", "Send"))
import login_rc
import reset_rc
