import datetime
import json
import re
import sys

import requests
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWidgets import *
from fbs_runtime.application_context.PyQt5 import ApplicationContext

from about import AboutForm
from login import LoginForm
from settings import UPDATE_URL, TNITBEST321JS, GET_COOKIE_URL
from utils import ImportExportLoginInfo, CustomQWebEngine


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        self.init_url = kwargs.get('init_url')
        self.ctx = kwargs.get('ctx')
        del kwargs['init_url']
        del kwargs['ctx']
        super(MainWindow, self).__init__(*args, **kwargs)
        self.initUi()

    def initUi(self):
        """Setting up for user login"""
        self.toolBar = QToolBar(self)
        self.toolBar.setMovable(False)

        # Add backward button
        self.backBtn = QPushButton(self)
        self.backBtn.setEnabled(False)
        self.backBtn.setIcon(QIcon(':/qt-project.org/styles/commonstyle/images/left-32.png'))
        self.backBtn.clicked.connect(self._back)
        self.toolBar.addWidget(self.backBtn)

        # Add forward button
        self.forBtn = QPushButton(self)
        self.forBtn.setEnabled(False)
        self.forBtn.setIcon(QIcon(':/qt-project.org/styles/commonstyle/images/right-32.png'))
        self.forBtn.clicked.connect(self._forward)
        self.toolBar.addWidget(self.forBtn)

        # Add address box
        self.address = QLineEdit(self)
        self.address.returnPressed.connect(self._load)
        self.address.setText(self.init_url)
        self.toolBar.addWidget(self.address)
        self.setFocus()

        # Add web engine view
        self._init_new_browser(self.init_url)

        # Setting window
        self.setWindowIcon(QIcon(self.ctx.get_resource("images/icon_facebook.png")))
        self.resize(QSize(800, 700))
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        self.setCentralWidget(self.browser)

        self.addToolBarBreak()
        self.addToolBar(Qt.TopToolBarArea, self.toolBar)
        self._create_action()
        self._create_menu_bar()

    def _init_new_browser(self, url):
        if hasattr(self, 'browser'):
            del self.browser
        self.browser = CustomQWebEngine()
        self.browser.setUrl(QUrl(url))
        self.browser.page().urlChanged.connect(self._on_load_finished)
        self.browser.page().titleChanged.connect(self.setWindowTitle)
        self.browser.page().urlChanged.connect(self._url_changed)

    def _create_menu_bar(self):
        menu_bar = QMenuBar(self)
        self.setMenuBar(menu_bar)

        function = QMenu('&Chức năng', self)
        function.addAction(self.update_cookie_action)
        function.addAction(self.update_token_action)
        function.addAction(self.login_with_cookie_action)
        function.addAction(self.exit_acction)
        menu_bar.addMenu(function)

        menu_bar.addAction(self.about_action)

    def _create_action(self):
        self.exit_acction = QAction(self)
        self.exit_acction.setText('Thoát')
        self.exit_acction.setShortcuts(QKeySequence(self.tr("Ctrl+Q")))
        self.exit_acction.triggered.connect(lambda self: sys.exit(1))

        self.login_with_cookie_action = QAction(self)
        self.login_with_cookie_action.setText('Đăng nhập bằng cookie')
        self.login_with_cookie_action.setIcon(QIcon(self.ctx.get_resource('images/icons_cookie.png')))
        self.login_with_cookie_action.setShortcuts(QKeySequence(self.tr("Ctrl+C")))
        self.login_with_cookie_action.triggered.connect(self.login_with_cookie)

        self.update_cookie_action = QAction(self)
        self.update_cookie_action.setText('Cập nhật cookie')
        self.update_cookie_action.setIcon(QIcon(self.ctx.get_resource('images/icon_up.png')))
        self.update_cookie_action.setShortcuts(QKeySequence(self.tr("Ctrl+U")))
        self.update_cookie_action.triggered.connect(self.update_cookie)

        self.update_token_action = QAction(self)
        self.update_token_action.setText('Cập nhật access token')
        self.update_token_action.setIcon(QIcon(self.ctx.get_resource('images/icon_key.png')))
        self.update_token_action.setShortcuts(QKeySequence(self.tr("Ctrl+A")))
        self.update_token_action.triggered.connect(self.update_access_token)

        self.about_action = QAction(self)
        self.about_action.setText('&Giới thiệu')
        self.about_action.triggered.connect(self._about)

    def _load(self):
        url = QUrl.fromUserInput(self.address.text())
        if url.isValid():
            self.browser.setUrl(url)

    def _back(self):
        self.browser.page().triggerAction(QWebEnginePage.Back)

    def _forward(self):
        self.browser.page().triggerAction(QWebEnginePage.Forward)

    def _url_changed(self, url):
        self.address.setText(url.toString())

    def _on_load_finished(self):
        if self.browser.history().canGoBack():
            self.backBtn.setEnabled(True)
        else:
            self.backBtn.setEnabled(False)

        if self.browser.history().canGoForward():
            self.forBtn.setEnabled(True)
        else:
            self.forBtn.setEnabled(False)

    def update_cookie(self):
        _TNITBEST321JS = dict()
        iei = ImportExportLoginInfo(self.ctx.get_resource(TNITBEST321JS))
        _TNITBEST321JS = iei.import_()
        headers = {
            "Authorization": f"{_TNITBEST321JS.get('token').get('token_type')} {_TNITBEST321JS.get('token').get('access_token')}",
            "s-key": f"{_TNITBEST321JS.get('secret_key')}"
        }
        # Get cookie on server first and keep sb, datr cookie if exist and not expired
        # It's took 2 years to expired datr, sb key name cookie
        response = requests.get(GET_COOKIE_URL, headers=headers)
        current_sb_datr = []
        if response.status_code == 200:
            cookies = response.json().get('cookies')
            for _cookie in cookies:
                if isinstance(_cookie, dict):
                    name = _cookie.get('name')
                    expiry = _cookie.get('expiry')
                    if (name and (name in ['sb', 'datr'])) and (expiry > datetime.datetime.now().timestamp()):
                        current_sb_datr.append(_cookie)

        if len(current_sb_datr) == 2:
            current_cookies = self.browser.get_cookies(except_cookies_name=['sb', 'datr'])
            current_cookies.extend(current_sb_datr)
        else:
            current_cookies = self.browser.get_cookies()


        # CHeck if user logged in or not
        is_logged_in = False
        for _cookie in current_cookies:
            name = _cookie.get('name')
            if not is_logged_in and name == "xs":
                is_logged_in = True
                break

        if not is_logged_in:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Thông báo")
            dlg.setText("Đăng nhập trước khi cập nhật cookie!")
            dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            dlg.setIcon(QMessageBox.Information)
            button = dlg.exec()
            return False

        response = requests.put(UPDATE_URL, json={'cookies': current_cookies}, headers=headers)

        if response.status_code == 200:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Thông báo")
            dlg.setText("Cập nhật cookie thành công")
            dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            dlg.setIcon(QMessageBox.Information)
            button = dlg.exec()
        else:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Thông báo")
            dlg.setText("Cập nhật cookie không thành công")
            dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            dlg.setInformativeText(response.text)
            dlg.setIcon(QMessageBox.Information)
            button = dlg.exec()

    def update_access_token(self):
        # CHeck if user logged in or not
        is_logged_in = False
        for _cookie in self.browser.get_cookies():
            name = _cookie.get('name')
            if not is_logged_in and name == "xs":
                is_logged_in = True
                break

        if not is_logged_in:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Thông báo")
            dlg.setText("Đăng nhập trước khi cập nhật access token!")
            dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            dlg.setIcon(QMessageBox.Information)
            button = dlg.exec()
            return False

        self.browser.setUrl(QUrl("https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed"))
        self.browser.loadFinished.connect(self.loaded_page_contain_access_token)

    def login_with_cookie(self):
        _TNITBEST321JS = dict()
        iei = ImportExportLoginInfo(self.ctx.get_resource(TNITBEST321JS))
        _TNITBEST321JS = iei.import_()
        headers = {
            "Authorization": f"{_TNITBEST321JS.get('token').get('token_type')} {_TNITBEST321JS.get('token').get('access_token')}",
            "s-key": f"{_TNITBEST321JS.get('secret_key')}"
        }
        response = requests.get(GET_COOKIE_URL, headers=headers)
        if response.status_code == 200:
            cookies = response.json().get('cookies')
            self.browser.setCookies(cookies)
            self.browser.reload()

    def loaded_page_contain_access_token(self):
        def find_in_html(html):
            access_token = re.search(r'(?P<access_token>EAAA\w+)', html)
            if access_token:
                access_token = access_token.groupdict().get('access_token')
                self.browser.setUrl(QUrl(self.init_url))
                _TNITBEST321JS = dict()
                iei = ImportExportLoginInfo(self.ctx.get_resource(TNITBEST321JS))
                _TNITBEST321JS = iei.import_()
                json = {
                    "access_token": access_token,
                }
                headers = {
                    "Authorization": f"{_TNITBEST321JS.get('token').get('token_type')} {_TNITBEST321JS.get('token').get('access_token')}",
                    "s-key": f"{_TNITBEST321JS.get('secret_key')}"
                }
                response = requests.put(UPDATE_URL, json=json, headers=headers)
                if response.status_code == 200:
                    dlg = QMessageBox(self)
                    dlg.setWindowTitle("Thông báo")
                    dlg.setText("Cập nhật token thành công")
                    dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                    dlg.setIcon(QMessageBox.Information)
                    button = dlg.exec()
                else:
                    dlg = QMessageBox(self)
                    dlg.setWindowTitle("Thông báo")
                    dlg.setText("Cập nhật token không thành công")
                    dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                    dlg.setInformativeText(response.text)
                    dlg.setIcon(QMessageBox.Information)
                    button = dlg.exec()

        self.browser.page().toHtml(find_in_html)

    def _about(self):
        self.about_window = QWidget()
        self.about_window.setWindowIcon(QIcon(self.ctx.get_resource("images/icon_facebook.png")))
        ui = AboutForm()
        ui.setupUi(self.about_window)
        self.about_window.show()


if __name__ == '__main__':
    appctxt = ApplicationContext()

    login_form = QWidget()
    login_form.setWindowIcon(QIcon(appctxt.get_resource("images/icon_facebook.png")))
    ui = LoginForm()
    ui.setupUi(login_form, ctx=appctxt)
    ui.setUpAfterLogin(MainWindow(init_url='https://www.facebook.com/', ctx=appctxt))
    login_form.show()

    sys.exit(appctxt.app.exec_())
