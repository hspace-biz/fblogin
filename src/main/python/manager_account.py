# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\src\main\resources\ui\manager_account.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Mananger_Account(object):
    def setupUi(self, Mananger_Account):
        Mananger_Account.setObjectName("Mananger_Account")
        Mananger_Account.resize(914, 596)
        self.gridLayout = QtWidgets.QGridLayout(Mananger_Account)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(Mananger_Account)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 50))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_search_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_search_btn.setGeometry(QtCore.QRect(0, 10, 186, 33))
        self.pushButton_search_btn.setMaximumSize(QtCore.QSize(82, 16777215))
        self.pushButton_search_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 170, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color:white;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../base/images/icons_search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_search_btn.setIcon(icon)
        self.pushButton_search_btn.setObjectName("pushButton_search_btn")
        self.textEdit_email = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit_email.setGeometry(QtCore.QRect(200, 10, 681, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_email.setFont(font)
        self.textEdit_email.setObjectName("textEdit_email")
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.lineEdit_search_text = QtWidgets.QLineEdit(Mananger_Account)
        self.lineEdit_search_text.setMaximumSize(QtCore.QSize(400, 16777215))
        self.lineEdit_search_text.setStyleSheet("QLineEdit {\n"
"   color: black;\n"
"   border-radius: 3px;\n"
"   padding: 10px 10px 10px;\n"
"   font-weight: bold;\n"
"   border: solid;\n"
"}")
        self.lineEdit_search_text.setObjectName("lineEdit_search_text")
        self.gridLayout.addWidget(self.lineEdit_search_text, 1, 0, 1, 1)
        self.scrollArea_ListAccount = QtWidgets.QScrollArea(Mananger_Account)
        self.scrollArea_ListAccount.setWidgetResizable(True)
        self.scrollArea_ListAccount.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea_ListAccount.setObjectName("scrollArea_ListAccount")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 892, 186))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_list_account = QtWidgets.QGridLayout()
        self.gridLayout_list_account.setObjectName("gridLayout_list_account")
        self.gridLayout_2.addLayout(self.gridLayout_list_account, 0, 0, 1, 1)
        self.scrollArea_ListAccount.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea_ListAccount, 6, 0, 1, 1)
        self.pushButton_add_cookie = QtWidgets.QPushButton(Mananger_Account)
        self.pushButton_add_cookie.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 170, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color:white;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}")
        self.pushButton_add_cookie.setAutoDefault(True)
        self.pushButton_add_cookie.setDefault(True)
        self.pushButton_add_cookie.setFlat(True)
        self.pushButton_add_cookie.setObjectName("pushButton_add_cookie")
        self.gridLayout.addWidget(self.pushButton_add_cookie, 9, 0, 1, 1)
        self.textEdit_cookie = QtWidgets.QTextEdit(Mananger_Account)
        self.textEdit_cookie.setStyleSheet("QTextEdit {\n"
"   color: black;\n"
"   border-radius: 3px;\n"
"   padding: 10px 10px 10px;\n"
"   font-weight: bold;\n"
"   border: solid;\n"
"}")
        self.textEdit_cookie.setObjectName("textEdit_cookie")
        self.gridLayout.addWidget(self.textEdit_cookie, 8, 0, 1, 1)
        self.label = QtWidgets.QLabel(Mananger_Account)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(Mananger_Account)
        QtCore.QMetaObject.connectSlotsByName(Mananger_Account)

    def retranslateUi(self, Mananger_Account):
        _translate = QtCore.QCoreApplication.translate
        Mananger_Account.setWindowTitle(_translate("Mananger_Account", "Mananger Account"))
        self.pushButton_search_btn.setText(_translate("Mananger_Account", "Tìm kiếm"))
        self.textEdit_email.setPlaceholderText(_translate("Mananger_Account", "Email của user cần chuyển giao tài khoản facebook"))
        self.lineEdit_search_text.setPlaceholderText(_translate("Mananger_Account", "Nhập văn bản cần tìm"))
        self.pushButton_add_cookie.setText(_translate("Mananger_Account", "Đăng nhập bằng cookie trên"))
        self.textEdit_cookie.setHtml(_translate("Mananger_Account", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:400;\"><br /></p></body></html>"))
        self.textEdit_cookie.setPlaceholderText(_translate("Mananger_Account", "Dán cookie có định dạng như sau để đăng nhập băng cookie datr=RXsTYElzufYQsOD7YOMQqnl6;c_user=100040540579117;fr=0G4w1NLVNj2tWZ7uF.AWWVSg1-0frATZawvuMYPr9WtkA.BhgMPs.B6.AAA.0.0.BhgMPu.AWU8k5Vkecg;sb=7MOAYWIqQ4x98jCbAuBgE8YK;wd=1920x937;xs=37%3AOPEdMMxY28H0jg%3A2%3A1635828718%3A-1%3A6224;spin=r.1004657483_b.trunk_t.1635828729_s.1_v.2_;"))
        self.label.setText(_translate("Mananger_Account", "Danh sách tài khoản facebook"))

