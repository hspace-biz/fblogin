import re
import sys

from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWidgets import *
from fbs_runtime.application_context.PyQt5 import ApplicationContext

from about import AboutForm
from login import LoginForm
from utils import CustomQWebEngine


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
        self.browser = CustomQWebEngine()
        self.browser.setUrl(QUrl(self.init_url))
        self.browser.page().urlChanged.connect(self._on_load_finished)
        self.browser.page().titleChanged.connect(self.setWindowTitle)
        self.browser.page().urlChanged.connect(self._url_changed)

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

    def _create_menu_bar(self):
        menu_bar = QMenuBar(self)
        self.setMenuBar(menu_bar)

        function = QMenu('&Chức năng', self)
        function.addAction(self.update_cookie_action)
        function.addAction(self.update_token_action)
        menu_bar.addMenu(function)

        menu_bar.addAction(self.about_action)

    def _create_action(self):
        self.update_cookie_action = QAction(self)
        self.update_cookie_action.setText('Cập nhật cookie')
        self.update_cookie_action.setIcon(QIcon(self.ctx.get_resource('images/icon_up.png')))
        self.update_cookie_action.triggered.connect(self.update_cookie)

        self.update_token_action = QAction(self)
        self.update_token_action.setText('Cập nhật access token')
        self.update_token_action.setIcon(QIcon(self.ctx.get_resource('images/icon_key.png')))
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
        print(self.browser.get_cookies())
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Thông báo")
        dlg.setText("Cập nhật thành công")
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setIcon(QMessageBox.Information)
        button = dlg.exec()

    def update_access_token(self):
        self.browser.setUrl(QUrl("https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed"))
        self.browser.loadFinished.connect(self.loaded_page_contain_access_token)

    def loaded_page_contain_access_token(self):
        def find_in_html(html):
            access_token = re.search(r'(?P<access_token>EAAA\w+)', html)
            if access_token:
                access_token = access_token.groupdict().get('access_token')
                print(access_token)
                self.browser.setUrl(QUrl(self.init_url))
                dlg = QMessageBox(self)
                dlg.setWindowTitle("Thông báo")
                dlg.setText("Cập nhật thành công")
                dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                dlg.setIcon(QMessageBox.Information)
                button = dlg.exec()

        self.browser.page().toHtml(find_in_html)

    def _about(self):
        self.about_window = QWidget()
        self.about_window.setWindowIcon(QIcon(self.ctx.get_resource("images/icon_facebook.png")))
        ui = AboutForm()
        ui.setupUi(self.about_window)
        self.about_window.show()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        QSqlDatabase.removeDatabase(QSqlDatabase.database().connectionName())


if __name__ == '__main__':
    appctxt = ApplicationContext()

    login_form = QWidget()
    login_form.setWindowIcon(QIcon(appctxt.get_resource("images/icon_facebook.png")))
    ui = LoginForm()
    ui.setupUi(login_form)
    ui.setUpAfterLogin(MainWindow(init_url='https://www.facebook.com', ctx=appctxt))
    login_form.show()

    sys.exit(appctxt.app.exec_())
