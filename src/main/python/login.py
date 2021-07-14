import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from settings import LOGIN_URL, TNITBEST321JS


class LoginForm(object):
    def setupUi(self, Form):
        # For controlling form
        self._form = Form
        # Init UI for login form
        Form.setObjectName("Form")
        Form.resize(533, 393)
        Form.setMinimumSize(QtCore.QSize(533, 393))
        Form.setMaximumSize(QtCore.QSize(533, 393))
        Form.setStyleSheet("background: white")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setEnabled(False)
        self.textEdit.setGeometry(QtCore.QRect(-10, -10, 551, 81))
        self.textEdit.setAcceptDrops(True)
        self.textEdit.setAutoFillBackground(True)
        self.textEdit.setStyleSheet("border: none")
        self.textEdit.setObjectName("textEdit")
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(80, 80, 371, 171))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.password = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.password.setStyleSheet("QLineEdit {\n"
                                    "    border: 1px solid gray;\n"
                                    "    border-radius: 3px;\n"
                                    "    padding: 8px;\n"
                                    "    background: white;\n"
                                    "    selection-background-color: darkgray;\n"
                                    "}")
        self.password.setObjectName("password")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.textChanged.connect(self._on_text_changed)
        self.gridLayout_3.addWidget(self.password, 4, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.email = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.email.setStyleSheet("QLineEdit {\n"
                                 "    border: 1px solid gray;\n"
                                 "    border-radius: 3px;\n"
                                 "    padding: 8px;\n"
                                 "    background: white;\n"
                                 "    selection-background-color: darkgray;\n"
                                 "}")
        self.email.setPlaceholderText("")
        self.email.setObjectName("email")
        self.email.textChanged.connect(self._on_text_changed)
        self.gridLayout_3.addWidget(self.email, 0, 1, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(370, 330, 161, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.login_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.login_btn.setDisabled(True)
        self.login_btn.setStyleSheet("QPushButton {\n"
                                     "    border: 1px solid #8f8f91;\n"
                                     "    border-radius: 2px;\n"
                                     "    background-color: qlineargradient(spread:pad, x1:0.557, y1:0.414682, x2:0, y2:0, stop:0 rgba(7, 147, 124, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                     "    min-width: 80px;\n"
                                     "    padding: 13px;\n"
                                     "    color: white;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:pressed {\n"
                                     "    color: qlineargradient(spread:pad, x1:0.557, y1:0.414682, x2:0, y2:0, stop:0 rgba(7, 147, 124, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                     "    background-color: qlineargradient(spread:pad, x1:0.317864, y1:0.352, x2:1, y2:1, stop:0 rgba(7, 147, 124, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:flat {\n"
                                     "    border: none; /* no border for a flat push button */\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:default {\n"
                                     "    border-color: navy; /* make the default button prominent */\n"
                                     "}")
        self.login_btn.setDefault(True)
        self.login_btn.setFlat(True)
        self.login_btn.setObjectName("login_btn")
        self.login_btn.clicked.connect(self._login)
        self.login_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalLayout.addWidget(self.login_btn, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(80, 250, 371, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.forgot_pwd_btn = QtWidgets.QCommandLinkButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setItalic(False)
        self.forgot_pwd_btn.setFont(font)
        self.forgot_pwd_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.forgot_pwd_btn.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.forgot_pwd_btn.setStyleSheet("QPushButton {\n"
                                          "    border: none;\n"
                                          "    background-color: white;\n"
                                          "    min-width: 80px;\n"
                                          "    color: blue;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:pressed {\n"
                                          "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                          "                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
                                          "    text-decoration: underline;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:flat {\n"
                                          "    border: none; /* no border for a flat push button */\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:default {\n"
                                          "    border-color: navy; /* make the default button prominent */\n"
                                          "}\n"
                                          "")
        self.forgot_pwd_btn.setAutoDefault(False)
        self.forgot_pwd_btn.setDefault(True)
        self.forgot_pwd_btn.setObjectName("forgot_pwd_btn")
        self.horizontalLayout_2.addWidget(self.forgot_pwd_btn, 0, QtCore.Qt.AlignLeft)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Đăng nhập"))
        self.textEdit.setHtml(_translate("Form",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                         "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                         "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                         "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; color:#00aa7f;\">Đăng nhập FbSyncAccount</span></p></body></html>"))
        self.label.setText(_translate("Form",
                                      "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; text-decoration: underline;\">Mật khẩu</span></p></body></html>"))
        self.label_2.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; text-decoration: underline;\">Email</span></p></body></html>"))
        self.login_btn.setText(_translate("Form", "Đăng nhập"))
        self.forgot_pwd_btn.setText(_translate("Form", "Quên mật khẩu?"))

    def setUpAfterLogin(self, window: QMainWindow):
        self.window = window

    def _on_text_changed(self):
        self.login_btn.setEnabled(bool(self.email.text()) and bool(self.password.text()))

    def _login(self):
        # Get Email
        email = self.email.text()
        # Get Password
        pwd = self.password.text()

        response = requests.post(
            LOGIN_URL,
            json={
                'email': email,
                'password': pwd
            }
        )

        if response.status_code == 200:
            with open(TNITBEST321JS, 'w') as f:
                import json
                f.write(json.dumps(response.json()))
                f.close()
                self.window.show()
                self._form.close()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Kiểm tra lại thông tin đăng nhập!")
            msg.setInformativeText("Email/mật khẩu không tồn tại trên hệ thống")
            msg.setWindowTitle("Đăng nhập")
            msg.setDetailedText(f"{response.text}")
            msg.exec_()