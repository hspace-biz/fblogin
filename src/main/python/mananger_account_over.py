from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from settings import TNITBEST321JS, UID_TAGET
from utils import ImportExportLoginInfo
from manager_account import Ui_Mananger_Account
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidget, QTableWidgetItem, QDesktopWidget, QWidget
from PyQt5.QtCore import QSize, Qt
import time
import datetime


class Btn_facebook_action(QtWidgets.QPushButton):
    TYPE_UPDATE_DISABLE = 0
    TYPE_UPDATE_ENABLE = 1
    TYPE_UPDATE_COOLDOWN = 2
    TYPE_UPDATE_UNCOOLDOWN = 3
    TYPE_LOGIN = 4
    TYPE_DELETE = 5
    TYPE_COPY = 6
    TYPE_MOVE = 7

    def set_uid(self, uid: str, father, ctx,row:int, sub_email_new:str=None,is_move:bool=False) -> (None):
        """Set uid for button login
        Args:
            uid (str): this is uid will login facebook when button clicked
        Returns:
            None
        """  # """
        self.uid = uid
        self.father = father
        self.ctx = ctx
        self.sub_email_new=sub_email_new
        if self.sub_email_new is None:
            self.sub_email_new = "trash"
        self.is_move = is_move
        self.row = row
        

    def set_next_windown(self, window: QMainWindow):
        self.window = window

    def set_current_window(self, window: QMainWindow):
        self.current_window = window

    def action(self):
        if self.type_action == Btn_facebook_action.TYPE_LOGIN:
            self.login()
        elif self.type_action == Btn_facebook_action.TYPE_UPDATE_DISABLE:
            self.update_disable(True)
        elif self.type_action == Btn_facebook_action.TYPE_UPDATE_ENABLE:
            self.update_disable(False)
        elif self.type_action == Btn_facebook_action.TYPE_UPDATE_COOLDOWN:
            self.update_cooldown(True)
        elif self.type_action == Btn_facebook_action.TYPE_UPDATE_UNCOOLDOWN:
            self.update_cooldown(False)
        elif self.type_action == Btn_facebook_action.TYPE_DELETE:
            self.delete_facebook()
        elif self.type_action == Btn_facebook_action.TYPE_COPY:
            self.copy_facebook()

    def update_disable(self, flag: bool):
        print(f"set disable: {flag}")
        _TNITBEST321JS = dict()
        iei = ImportExportLoginInfo(self.ctx.get_resource(TNITBEST321JS))
        _TNITBEST321JS = iei.import_()
        headers = {
            "Authorization": f"{_TNITBEST321JS.get('token').get('token_type')} {_TNITBEST321JS.get('token').get('access_token')}",
            "s-key": f"{_TNITBEST321JS.get('secret_key')}"
        }
        BASE_URL = _TNITBEST321JS.get("BASE_URL")
        data_js = {"uid": self.uid, "is_disabled": flag}
        print(f"{BASE_URL}/update_account_by_uid")
        response = requests.put(
            f"{BASE_URL}/update_account_by_uid", headers=headers, json=data_js)
        self.current_window.load_data()
        print(response.text)

    def update_cooldown(self, flag: bool):
        print(f"set disable: {flag}")
        _TNITBEST321JS = dict()
        iei = ImportExportLoginInfo(self.ctx.get_resource(TNITBEST321JS))
        _TNITBEST321JS = iei.import_()
        headers = {
            "Authorization": f"{_TNITBEST321JS.get('token').get('token_type')} {_TNITBEST321JS.get('token').get('access_token')}",
            "s-key": f"{_TNITBEST321JS.get('secret_key')}"
        }
        BASE_URL = _TNITBEST321JS.get("BASE_URL")
        data_js = {"uid": self.uid, "is_cool_down": flag}
        print(f"{BASE_URL}/update_account_by_uid")
        response = requests.put(
            f"{BASE_URL}/update_account_by_uid", headers=headers, json=data_js)
        self.current_window.load_data()
    
    def delete_facebook(self):
        dlg = QMessageBox()
        dlg.setWindowTitle("Thông báo")
        dlg.setText(f"Bạn có muốn xóa tài khoản {self.uid} không?")
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setIcon(QMessageBox.Information)
        bttn = dlg.exec()
        if bttn == QMessageBox.Yes:
            self.__move_facebook(sub_email="trash",is_move=True)
        
    def copy_facebook(self):
        email = self.current_window.textEdit_email.toPlainText()
        if len(email)<=5:
            dlg = QMessageBox()
            dlg.setWindowTitle("Thông báo")
            dlg.setText(f"Hảy điền email thụ hưởng.")
            dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            dlg.setIcon(QMessageBox.Information)
            bttn = dlg.exec()
            return
        
        dlg = QMessageBox()
        dlg.setWindowTitle("Thông báo")
        dlg.setText(f"Bạn có muốn copy tài khoản {self.uid} cho {email} không?")
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setIcon(QMessageBox.Information)
        bttn = dlg.exec()
        if bttn == QMessageBox.Yes:
            self.__move_facebook(is_move=False,sub_email=email)
        
    def move_facebook(self):
        self.__move_facebook(is_move=True)
        
    def __move_facebook(self,sub_email:str = None,is_move:bool = None):
        _TNITBEST321JS = dict()
        iei = ImportExportLoginInfo(self.ctx.get_resource(TNITBEST321JS))
        _TNITBEST321JS = iei.import_()
        headers = {
            "Authorization": f"{_TNITBEST321JS.get('token').get('token_type')} {_TNITBEST321JS.get('token').get('access_token')}",
            "s-key": f"{_TNITBEST321JS.get('secret_key')}"
        }
        BASE_URL = _TNITBEST321JS.get("BASE_URL")
        
        if sub_email is None:
            sub_email = self.sub_email_new
        if is_move is None:
            is_move = self.is_move
            
        data_js = {"pid": self.uid, "sub_email": sub_email,"move":is_move}
        print(f"{BASE_URL}/copy_facebook_account")
        response = requests.put(
            f"{BASE_URL}/copy_facebook_account", headers=headers, json=data_js)
        if response.status_code==200:
            dlg = QMessageBox()
            dlg.setWindowTitle("Thông báo")
            dlg.setText(f"Thực hiện tác vụ thành công\n{response.json().get('msg')}.")
            dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            dlg.setIcon(QMessageBox.Information)
            bttn = dlg.exec() 
        else:
            dlg = QMessageBox()
            dlg.setWindowTitle("Thông báo")
            dlg.setText(f"Thực hiện tác vụ thất bị.\n{response.text}.")
            dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            dlg.setIcon(QMessageBox.Information)
            bttn = dlg.exec() 
        self.current_window.load_data()
    
    def login(self):
        """Login to facebook with uid set in set_uid function"""
        self.window.show()
        self.window.login_with_cookie(uid_taget=self.uid)
        self.father.close()

    def set_type(self, _type: int):
        self.type_action = _type
        
    def delete(self):
        """Move this account to trash
        """
        pass
    


class Mananger_account(Ui_Mananger_Account):
    def setupUi(self, Form, ctx):
        super().setupUi(Form)
        self.ctx = ctx
        self.Form = Form
        self.total_row = 0
        self.data = []
        self.load_data()
        self.pushButton_add_cookie.clicked.connect(self.login_with_cookie)
        self.pushButton_search_btn.clicked.connect(self.search_btn_click)
        self.lineEdit_search_text.textChanged.connect(self.search_text_change)
        
    def login_with_cookie(self):
        cookies_raw = self.textEdit_cookie.toPlainText().split(";")
        cookies = []
        for cookie in cookies_raw:
            cookie = cookie.split("=")
            if len(cookie) < 2:
                continue
            _cookie = {}
            _cookie["name"] = cookie[0]
            _cookie["value"] = cookie[1]
            _cookie["path"] = "/"
            _cookie["expiry"] = 1668244048  # TODO: sua cho nay lai
            _cookie["secure"] = True
            _cookie["httpOnly"] = False
            _cookie["sameSite"] = 'None'
            cookies.append(_cookie)
        self.window.login_with_cookie_input(cookies=cookies)
        self.window.show()
        self.Form.close()
        
    def load_data(self):

        _TNITBEST321JS = dict()
        iei = ImportExportLoginInfo(self.ctx.get_resource(TNITBEST321JS))
        _TNITBEST321JS = iei.import_()
        headers = {
            "Authorization": f"{_TNITBEST321JS.get('token').get('token_type')} {_TNITBEST321JS.get('token').get('access_token')}",
            "s-key": f"{_TNITBEST321JS.get('secret_key')}"
        }
        BASE_URL = _TNITBEST321JS.get("BASE_URL")
        response = requests.get(
            f"{BASE_URL}/get_all_my_facebook_account", headers=headers)
        self.data_js = {}
        if response.status_code == 200:

            try:
                data_temp = json.loads(response.text)
                self.data_js = data_temp
            except:
                pass
        self.data = self.data_js.get("data")
        self.load_data_to_view(self.data)

    def load_data_to_view(self, data):
        """This function arm to render data to grid layout"""
        # First need to clean the layout
        # for i in reversed(range(self.gridLayout_list_account.count())):
        #     self.gridLayout_list_account.itemAt(i).widget().setParent(None)

        if data:
            for i in reversed(range(self.gridLayout_list_account.count())):
                self.gridLayout_list_account.itemAt(i).widget().setParent(None)
                # self.gridLayout_list_account.itemAt(i).widget().deleteLater()

            self.login_map = {}
            self.gridLayout_list_account.setAlignment(Qt.AlignTop)
            icon_cp = QtGui.QIcon()
            icon_cp.addFile(self.ctx.get_resource("images/copy.png"),size=QSize(30,30))
            
            icon_delete = QtGui.QIcon()
            icon_delete.addFile(self.ctx.get_resource("images/delete.png"),size=QSize(30,30))
            for row, data in enumerate(data):
                col = 0
                action_facebook_button = Btn_facebook_action()
                action_facebook_button.setFixedWidth(150)
                self.gridLayout_list_account.addWidget(
                    action_facebook_button, row, col, Qt.AlignLeft)
                uid = None
                for cookie in data["cookies"]:
                    if cookie.get("name") == "c_user":
                        uid = cookie.get("value")
                        break
                action_facebook_button.set_uid(
                    uid=str(cookie.get('value')), father=self.Form, ctx=self.ctx,row=row)
                action_facebook_button.set_current_window(self)
                action_facebook_button.set_type(
                    _type=Btn_facebook_action.TYPE_LOGIN)
                action_facebook_button.clicked.connect(
                    action_facebook_button.action)
                action_facebook_button.set_next_windown(window=self.window)
                action_facebook_button.setText(f"Login to :{uid}")

                col += 1
                action_facebook_button = Btn_facebook_action()
                action_facebook_button.set_uid(
                    uid=str(cookie.get('value')), father=self.Form, ctx=self.ctx,row=row)
                action_facebook_button.setFixedWidth(30)
                
                action_facebook_button.setIcon(icon_delete)
                self.gridLayout_list_account.addWidget(
                    action_facebook_button, row, col, Qt.AlignLeft)
                action_facebook_button.set_type(Btn_facebook_action.TYPE_DELETE)
                action_facebook_button.set_current_window(self)
                action_facebook_button.clicked.connect(
                    action_facebook_button.action)

                col += 1
                action_facebook_button = Btn_facebook_action()
                action_facebook_button.set_uid(
                    uid=str(cookie.get('value')), father=self.Form, ctx=self.ctx,row=row)
                action_facebook_button.setFixedWidth(30)
                
                action_facebook_button.setIcon(icon_cp)
                self.gridLayout_list_account.addWidget(
                    action_facebook_button, row, col, Qt.AlignLeft)
                action_facebook_button.set_type(Btn_facebook_action.TYPE_COPY)
                action_facebook_button.set_current_window(self)
                action_facebook_button.clicked.connect(
                    action_facebook_button.action)
                
                
                col += 1
                lable = QtWidgets.QLabel()
                lable.setFixedWidth(180)
                self.gridLayout_list_account.addWidget(
                    lable, row, col, Qt.AlignLeft)
                lable.setText(f"Name:{data.get('name')}")

                col += 1
                action_facebook_button = Btn_facebook_action()
                action_facebook_button.setFixedWidth(100)
                self.gridLayout_list_account.addWidget(
                    action_facebook_button, row, col, Qt.AlignLeft)
                action_facebook_button.set_uid(
                    uid=str(cookie.get('value')), father=self.Form, ctx=self.ctx,row=row)
                action_facebook_button.set_current_window(self)
                action_facebook_button.clicked.connect(
                    action_facebook_button.action)
                if data.get("is_disabled") == False:
                    action_facebook_button.set_type(
                        _type=Btn_facebook_action.TYPE_UPDATE_DISABLE)
                    action_facebook_button.setText(f"Disable")
                    self.set_color_button(action_facebook_button, 0, 100, 0)
                else:
                    action_facebook_button.set_type(
                        _type=Btn_facebook_action.TYPE_UPDATE_ENABLE)
                    action_facebook_button.setText(f"Enable")
                    self.set_color_button(action_facebook_button, 255, 0, 0)


                col += 1
                list_email = QtWidgets.QComboBox()
                list_email.setFixedWidth(300)
                for email in data.get("email"):
                    list_email.addItem(email)
                self.gridLayout_list_account.addWidget(
                    list_email, row, col, Qt.AlignLeft)
                
                
                col += 1
                action_facebook_button = Btn_facebook_action()
                action_facebook_button.setFixedWidth(100)
                self.gridLayout_list_account.addWidget(
                    action_facebook_button, row, col, Qt.AlignLeft)
                action_facebook_button.set_uid(
                    uid=str(cookie.get('value')), father=self.Form, ctx=self.ctx,row=row)
                action_facebook_button.set_current_window(self)
                action_facebook_button.clicked.connect(
                    action_facebook_button.action)
                if data.get("is_cooldown") == False:
                    action_facebook_button.set_type(
                        _type=Btn_facebook_action.TYPE_UPDATE_COOLDOWN)
                    action_facebook_button.setText(f"Cooldown")
                    self.set_color_button(action_facebook_button, 0, 100, 0)
                else:
                    action_facebook_button.set_type(
                        _type=Btn_facebook_action.TYPE_UPDATE_UNCOOLDOWN)
                    action_facebook_button.setText(f"UnCooldown")
                    self.set_color_button(action_facebook_button, 255, 0, 0)

                col += 1
                time_remain = QtWidgets.QLabel()
                # No need to set fixed width
                # time_remain.setFixedWidth(200)
                self.gridLayout_list_account.addWidget(
                    time_remain, row, col, Qt.AlignLeft)
                y_d_h_m_s = str(datetime.timedelta(
                    float(data.get('remain_time_cool_down').replace("(s)", "").replace("s", "")))) if data.get('remain_time_cool_down') else None
                time_remain.setText(
                    f"Time cooldow:{y_d_h_m_s}")

                # Update number of rows has been inserted to the layout
                self.total_row += 1

    def set_color_button(self, ob, r, g, b):
        color = QtGui.QColor(r, g, b)
        alpha = 140
        values = "{r}, {g}, {b}, {a}".format(r=color.red(),
                                             g=color.green(),
                                             b=color.blue(),
                                             a=alpha
                                             )
        print(type(ob))
        ob.setStyleSheet("QPushButton { background-color: rgba("+values+"); }")

    def login_to_system(self, this_btn):
        print(f"{int(time.time())}:Login with uid: " +
              self.login_map[this_btn.__hash__])
        print(this_btn.__hash__)

    def search_btn_click(self):
        # Get text from search line edit
        text = self.lineEdit_search_text.text()
        if len(text) == 0:
            self.lineEdit_search_text.setPlaceholderText(
                "Vui lòng nhập UID cần tìm vào đây hoặc gõ 'all' để hiển thị đầy đủ!")
            self.lineEdit_search_text.setStyleSheet("QLineEdit {\n"
                                                    "   color: red;\n"
                                                    "   border-radius: 3px;\n"
                                                    "   padding: 10px 10px 10px;\n"
                                                    "   font-weight: bold;\n"
                                                    "   border: solid;\n"
                                                    "}")
        elif text != 'all':
            # Filter action base one re-fetched data
            self.filted_data = []
            for item_data in self.data:
                for item_cookie in item_data['cookies']:
                    if item_cookie['name'] == 'c_user' and text in item_cookie['value']:
                        self.filted_data.append(item_data)
                        break
            self.load_data_to_view(self.filted_data)
        else:
            self.load_data_to_view(self.data)

    def search_text_change(self):
        self.lineEdit_search_text.setStyleSheet("QLineEdit {\n"
                                                "   color: black;\n"
                                                "   border-radius: 3px;\n"
                                                "   padding: 10px 10px 10px;\n"
                                                "   font-weight: bold;\n"
                                                "   border: solid;\n"
                                                "}")
        self.lineEdit_search_text.setPlaceholderText(
            "Nhập văn bản cần tìm")

    def retranslateUi(self, Mananger_Account):
        super().retranslateUi(Mananger_Account)

    def setUpAfterLogin(self, window: QMainWindow):
        self.window = window
