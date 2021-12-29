import datetime
import json
import re
import sys
from time import time,sleep

import requests
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWidgets import *
from fbs_runtime.application_context.PyQt5 import ApplicationContext

from about import AboutForm
from login import LoginForm
from mananger_account_over import Mananger_account
from settings import TNITBEST321JS
from utils import ImportExportLoginInfo, CustomQWebEngine
import inspect

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        self.init_url = kwargs.get('init_url')
        self.ctx = kwargs.get('ctx')
        self.From = kwargs.get('From')
        del kwargs['init_url']
        del kwargs['ctx']
        super(MainWindow, self).__init__(*args, **kwargs)
        self.uid_taget = None
        self.wait_dlg = None
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
        self.browser = None
        # Add web engine view
        self._init_new_browser(self.init_url)

        # Setting window
        self.setWindowIcon(QIcon(self.ctx.get_resource("images/icon_sync.png")))
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
   
        if self.browser:
            self.browser.clean_cookies
        self.browser = CustomQWebEngine()
        
        self.browser.setUrl(QUrl(url))
        self.browser.page().urlChanged.connect(self._on_load_finished)
        self.browser.page().titleChanged.connect(self.setWindowTitle)
        self.browser.page().urlChanged.connect(self._url_changed)
        self.browser.load(QUrl(url))
        self.setCentralWidget(self.browser)


    def _create_menu_bar(self):
        menu_bar = QMenuBar(self)
        self.setMenuBar(menu_bar)

        function = QMenu('&Chức năng', self)
        function.addAction(self.update_cookie_action)

        function.addAction(self.exit_acction)
        menu_bar.addMenu(function)

        menu_bar.addAction(self.about_action)
        menu_bar.addAction(self.list_account_facebook_action)

    def _create_action(self):
        self.exit_acction = QAction(self)
        self.exit_acction.setText('Thoát')
        self.exit_acction.setShortcuts(QKeySequence(self.tr("Ctrl+Q")))
        self.exit_acction.triggered.connect(lambda self: sys.exit(1))


        self.update_cookie_action = QAction(self)
        self.update_cookie_action.setText('Cập nhật cookie')
        self.update_cookie_action.setIcon(QIcon(self.ctx.get_resource('images/icon_up.png')))
        self.update_cookie_action.setShortcuts(QKeySequence(self.tr("Ctrl+U")))
        self.update_cookie_action.triggered.connect(self.update_cookie)

        self.about_action = QAction(self)
        self.about_action.setText('&Giới thiệu')
        self.about_action.triggered.connect(self._about)
        
        self.list_account_facebook_action = QAction(self)
        self.list_account_facebook_action.setText('&D.sách t.khoản')
        self.list_account_facebook_action.triggered.connect(self.__manager_account__)
        self.is_update = False

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

    def __set_name__(self,result):
        current_url = str(self.browser.url().url())
     
        self.browser.load(QUrl(f"https://mbasic.facebook.com/{self.uid_taget}"))
        self.browser.loadFinished.connect(lambda x:self.browser.page().runJavaScript(
                "document.evaluate(\"//*[@id='root']//strong\", document.body, null, XPathResult.STRING_TYPE, null).stringValue", self.__set_name__
            ))
            
        self.browser.loadFinished.disconnect()
        self.name_user = result
        self.browser.page().runJavaScript(
            "document.evaluate(\"//*[@id='root']//div/a[contains(@href,'/photo.php')]/img[contains(@alt,'profile picture')]/@src\", document.body, null, XPathResult.STRING_TYPE, null).stringValue", self.__set_avatar__
        )
        return False
    def __set_avatar__(self,result):
        self.avatar_url = result
        self.__update_cookie()
        return True
        
    def __set_c_friends__(self,result:str):
        self.browser.loadFinished.disconnect()
        if result is not None:
            result = result.split(" ")[-1].replace("(","").replace(")","")
            try:
                result = int(result)
            except:
                result = None
        
        self.c_friends = result
        
        
    
        
    def _on_load_finished(self):
        pass
 
        
    def update_cookie(self):
        if self.wait_dlg is None:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Thông báo")
            dlg.setText(f"Bắt đầu cập nhật cookie, vui lòng chờ vài giây.")
            dlg.setIcon(QMessageBox.Information)
            dlg.show()
            self.wait_dlg = dlg
            self.uid_taget is None


        if self.uid_taget is None:
            self.browser.load(QUrl(f"https://mbasic.facebook.com"))
            self.browser.loadFinished.connect(lambda x:self.browser.page().runJavaScript(
                    "document.evaluate(\"//a[contains(@href,'a/like.php')]/@href\", document.body, null, XPathResult.STRING_TYPE, null).stringValue.split(\"&av=\")[1].split(\"&\")[0]", self.__get_uid_taget__
                ))
        else:
            self.browser.load(QUrl(f"https://mbasic.facebook.com/profile.php?_rdr"))
            self.browser.loadFinished.connect(lambda x:self.browser.page().runJavaScript(
                    "document.evaluate(\"//*[@id='root']//strong\", document.body, null, XPathResult.STRING_TYPE, null).stringValue", self.__set_name__
                ))

 
    def __get_uid_taget__(self,result:str):
        try:
            self.browser.loadFinished.disconnect()
            self.uid_taget = result
            self.update_cookie()
        except Exception as ex:
            if self.wait_dlg is not None:
                self.wait_dlg.close()
                self.wait_dlg = None
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Thông báo")
            dlg.setText(f"Error: {ex}")
            dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            dlg.setIcon(QMessageBox.Information)
            dlg.exec()
            
        return False
        
        
    def __update_cookie(self):
        if self.wait_dlg is not None:
            self.wait_dlg.close()
            self.wait_dlg = None
        update_name = True
        
        self.avatar_url = str(self.avatar_url)
        self.name_user = str(self.name_user)
        
        # if self.name_user is None or len(self.name_user)<=3 or self.avatar_url is None or len(self.avatar_url)<=len("https://"):
        #     dlg = QMessageBox(self)
        #     dlg.setWindowTitle("Thông báo")
        #     dlg.setText(f"Không tìm thấy thông tin tài khoản hoặc thông tin tài khoản sai:\n*Name: {self.name_user}\n*Avatar url: {self.avatar_url}")
        #     dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        #     dlg.setIcon(QMessageBox.Information)
        #     dlg.exec()
        #     update_name = False
            
        #     return False
            # return False
        # self.browser.setUrl(QUrl(f"https://www.facebook.com/{self.uid_taget}"))
        print(f'user name: {self.name_user}')
        print(f'avatar url: {self.avatar_url}')
        _TNITBEST321JS = dict()
        iei = ImportExportLoginInfo(self.ctx.get_resource(TNITBEST321JS))
        _TNITBEST321JS = iei.import_()
        
        headers = {
            "Authorization": f"{_TNITBEST321JS.get('token').get('token_type')} {_TNITBEST321JS.get('token').get('access_token')}",
            "s-key": f"{_TNITBEST321JS.get('secret_key')}"
        }
        # Get cookie on server first and keep sb, datr cookie if exist and not expired
        # It's took 2 years to expired datr, sb key name cookie
        BASE_URL = _TNITBEST321JS.get("BASE_URL")
        response = requests.get(f"{BASE_URL}/get-my-fb-account-cookie", headers=headers)
        current_sb_datr = []
 
        current_cookies = []
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
            dlg.exec()
            
            return True

        payload = {'cookies': current_cookies}
        print(f"Current cookies: {current_cookies}")
        if update_name:
            payload = {'cookies': current_cookies,'name':self.name_user,'avatar_url':self.avatar_url}

        response = requests.put(f"{BASE_URL}/update-my-fb-account-secret", json=payload, headers=headers)
        print(f"Current cookies: {response.text}")
        if response.status_code == 200:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Thông báo")
            dlg.setText("Cập nhật cookie thành công")
            dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            dlg.setIcon(QMessageBox.Information)
            dlg.exec()
            
            return False
        elif response.status_code==400:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Thông báo")
            dlg.setText("Cập nhật cookie không thành công")
            dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            dlg.setInformativeText(f"Phiên đăng nhập hiện tại của tài khoản đã kết thúc do tài khoản đã được đăng nhập ở nơi khác.")
            dlg.setIcon(QMessageBox.Information)
            dlg.exec()
            return False
        else:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Thông báo")
            dlg.setText("Cập nhật cookie không thành công")
            dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            dlg.setInformativeText(f"Error: {response.status_code} -- {response.text}")
            dlg.setIcon(QMessageBox.Information)
            dlg.exec()
            return False

    def update_access_token(self):
        pass
    
    def login_with_cookie_input(self,cookies):
        self._init_new_browser('https://www.facebook.com')
        print(cookies)
        self.browser.setCookies(cookies)
        self.browser.setUrl(QUrl('https://mbasic.facebook.com'))
        
        
    
    def login_with_cookie(self,uid_taget:str =None):
        
        """auto get cookie with c_user is uid and login to facebook

        Args:
            uid (str, optional): uid is valTuyet123456ue of c_user in cookie, if uid is None then cookie get is cookie available. Defaults to None.
        """
        self.uid_taget = uid_taget
        _TNITBEST321JS = dict()
        iei = ImportExportLoginInfo(self.ctx.get_resource(TNITBEST321JS))
        _TNITBEST321JS = iei.import_()
        headers = {
            "Authorization": f"{_TNITBEST321JS.get('token').get('token_type')} {_TNITBEST321JS.get('token').get('access_token')}",
            "s-key": f"{_TNITBEST321JS.get('secret_key')}"
        }
        payload = {"uid":uid_taget}
        print(payload)
        print(payload)
        BASE_URL = _TNITBEST321JS.get("BASE_URL")
        response = requests.get(f"{BASE_URL}/get-my-fb-account-cookie", headers=headers,json=payload)
        self._init_new_browser('https://www.facebook.com')
        if response.status_code == 200:
            cookies = response.json().get('cookies')
            self.browser.setCookies(cookies)
            self.browser.reload()
            self.browser.setUrl(QUrl(f"https://www.facebook.com/{self.uid_taget}"))
        self.uid_taget = None
        

    def _about(self):
        self.about_window = QWidget()
        self.about_window.setWindowIcon(QIcon(self.ctx.get_resource("images/icon_sync.png")))
        ui = AboutForm()
        ui.setupUi(self.about_window)
        self.about_window.show()
    
    def __manager_account__(self):
        self.manager_window = QWidget()
        self.manager_window.setWindowIcon(QIcon(self.ctx.get_resource("images/icon_sync.png")))
        ui = Mananger_account()
        ui.setUpAfterLogin(window=MainWindow(init_url='https://www.facebook.com/', ctx=self.ctx))
        ui.setupUi(self.manager_window,self.ctx)
        self.manager_window.show()
        self.close()
    
    def __reset_cookie__(self):
        pass


if __name__ == '__main__':
    appctxt = ApplicationContext()

    login_form = QWidget()
    login_form.setWindowIcon(QIcon(appctxt.get_resource("images/icon_sync.png")))
    ui = LoginForm()
    ui.setupUi(login_form, ctx=appctxt)
    ui.setUpAfterLogin(MainWindow(init_url='https://www.facebook.com/', ctx=appctxt))
    login_form.show()

    sys.exit(appctxt.app.exec_())
