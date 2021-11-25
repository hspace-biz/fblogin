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
        self.textEdit_cookie = QtWidgets.QTextEdit(Mananger_Account)
        self.textEdit_cookie.setObjectName("textEdit_cookie")
        self.gridLayout.addWidget(self.textEdit_cookie, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(Mananger_Account)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.scrollArea_ListAccount = QtWidgets.QScrollArea(Mananger_Account)
        self.scrollArea_ListAccount.setWidgetResizable(True)
        self.scrollArea_ListAccount.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea_ListAccount.setObjectName("scrollArea_ListAccount")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 892, 246))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_list_account = QtWidgets.QGridLayout()
        self.gridLayout_list_account.setObjectName("gridLayout_list_account")
        self.gridLayout_2.addLayout(self.gridLayout_list_account, 0, 0, 1, 1)
        self.scrollArea_ListAccount.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea_ListAccount, 1, 0, 1, 1)
        self.pushButton_add_cookie = QtWidgets.QPushButton(Mananger_Account)
        self.pushButton_add_cookie.setObjectName("pushButton_add_cookie")
        self.gridLayout.addWidget(self.pushButton_add_cookie, 4, 0, 1, 1)

        self.retranslateUi(Mananger_Account)
        QtCore.QMetaObject.connectSlotsByName(Mananger_Account)

    def retranslateUi(self, Mananger_Account):
        _translate = QtCore.QCoreApplication.translate
        Mananger_Account.setWindowTitle(_translate("Mananger_Account", "Mananger Account"))
        self.textEdit_cookie.setHtml(_translate("Mananger_Account", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI,Arial\'; font-size:12pt;\">datr=RXsTYElzufYQsOD7YOMQqnl6;c_user=100040540579117;fr=0G4w1NLVNj2tWZ7uF.AWWVSg1-0frATZawvuMYPr9WtkA.BhgMPs.B6.AAA.0.0.BhgMPu.AWU8k5Vkecg;sb=7MOAYWIqQ4x98jCbAuBgE8YK;wd=1920x937;xs=37%3AOPEdMMxY28H0jg%3A2%3A1635828718%3A-1%3A6224;spin=r.1004657483_b.trunk_t.1635828729_s.1_v.2_;</span></p></body></html>"))
        self.label.setText(_translate("Mananger_Account", "Danh sách tài khoản facebook"))
        self.pushButton_add_cookie.setText(_translate("Mananger_Account", "Đăng nhập bằng cooke"))

