import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from settings import TNITBEST321JS
from utils import ImportExportLoginInfo

BASE_URL = None

class LoginForm(object):
    def setupUi(self, Form, ctx):
        # For controlling form
        self._form = Form
        self.ctx = ctx
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
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 90, 511, 291))
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
                                    "}\n"
                                    "\n"
                                    "QLineEdit:focus {\n"
                                    "    border: 1px solid #00aa7f;\n"
                                    "}")
        self.password.setInputMask("")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.gridLayout_3.addWidget(self.password, 6, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.email = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.email.setStyleSheet("QLineEdit {\n"
                                 "    border: 1px solid gray;\n"
                                 "    border-radius: 3px;\n"
                                 "    padding: 8px;\n"
                                 "    background: white;\n"
                                 "    selection-background-color: darkgray;\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit:focus {\n"
                                 "    border: 1px solid #00aa7f;\n"
                                 "}")
        self.email.setObjectName("email")
        self.gridLayout_3.addWidget(self.email, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 6, 0, 1, 1)
        self.crawlerUrl = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.crawlerUrl.setStyleSheet("QLineEdit {\n"
                                      "    border: 1px solid gray;\n"
                                      "    border-radius: 3px;\n"
                                      "    padding: 8px;\n"
                                      "    background: white;\n"
                                      "    selection-background-color: darkgray;\n"
                                      "}\n"
                                      "\n"
                                      "QLineEdit:focus {\n"
                                      "    border: 1px solid #00aa7f;\n"
                                      "}")
        self.crawlerUrl.setObjectName("crawlerUrl")
        self.gridLayout_3.addWidget(self.crawlerUrl, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.forgot_pwd_btn = QtWidgets.QCommandLinkButton(self.gridLayoutWidget)
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
        self.gridLayout_3.addWidget(self.forgot_pwd_btn, 7, 0, 1, 1)
        self.login_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.login_btn.setEnabled(True)
        self.login_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.login_btn.setStyleSheet("QPushButton {\n"
                                     "    border: 1px solid #00aa7f;\n"
                                     "    border-radius: 2px;\n"
                                     "    background-color:#00aa7f;\n"
                                     "    min-width: 80px;\n"
                                     "    padding: 13px;\n"
                                     "    color: white;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:pressed {\n"
                                     "    color: #00aa7f;\n"
                                     "    background-color: #ffffff;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:hover {\n"
                                     "    color: #00aa7f;\n"
                                     "    background-color: #ffffff;\n"
                                     "    border: 1px solid #00aa7f;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:default {\n"
                                     "    border-color: #00aa7f; /* make the default button prominent */\n"
                                     "}")
        self.login_btn.setDefault(True)
        self.login_btn.setFlat(True)
        self.login_btn.setObjectName("login_btn")
        self.gridLayout_3.addWidget(self.login_btn, 7, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.crawlerUrl, self.email)
        Form.setTabOrder(self.email, self.password)
        Form.setTabOrder(self.password, self.login_btn)
        Form.setTabOrder(self.login_btn, self.textEdit)
        self.email.textChanged.connect(self._on_text_changed)
        self.crawlerUrl.textChanged.connect(self._on_text_changed)
        self.login_btn.clicked.connect(self._login)


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
        self.password.setPlaceholderText(_translate("Form", "Nhập mật khẩu đăng nhập hệ thống"))
        self.label_2.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#00aa7f;\">Email</span></p></body></html>"))
        self.email.setPlaceholderText(_translate("Form", "Nhập địa chỉ email tài khoản hệ thống"))
        self.label.setText(_translate("Form",
                                      "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#00aa7f;\">Mật khẩu</span></p></body></html>"))
        self.crawlerUrl.setPlaceholderText(_translate("Form", "Nhập địa chỉ url điều khiển crawler"))
        self.label_3.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#00aa7f;\">CrawlerURL</span></p></body></html>"))
        self.forgot_pwd_btn.setText(_translate("Form", "Quên mật khẩu?"))
        self.login_btn.setText(_translate("Form", "Đăng nhập >"))

    def setUpAfterLogin(self, window: QMainWindow):
        self.window = window

    def _on_text_changed(self):
        global BASE_URL
        BASE_URL = self.crawlerUrl.text()

    def _login(self):
        if not BASE_URL:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Thiếu CrawlUrl")
            msg.setInformativeText("Vui lòng nhập CrawlUrl!")
            msg.setWindowTitle("Thông báo")
            msg.exec_()
            return
        # Get Email
        email = self.email.text()
        # Get Password
        pwd = self.password.text()

        response = requests.post(
            f"{BASE_URL}/login",
            json={
                'email': email,
                'password': pwd
            }
        )

        if response.status_code == 200:
            data: dict = response.json()
            data["BASE_URL"] = BASE_URL
            iei = ImportExportLoginInfo(self.ctx.get_resource(TNITBEST321JS), data)
            iei.export()
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
