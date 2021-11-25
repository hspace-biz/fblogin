import datetime
import re
from typing import List

from PyQt5.QtCore import QDateTime
from PyQt5.QtNetwork import QNetworkCookie
from PyQt5.QtWebEngineWidgets import QWebEngineProfile, QWebEngineView
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel, QMessageBox
import json



def disable_account(uid:str):
    pass

class CustomQWebEngine(QWebEngineView):

    def __init__(self, *args, **kwargs):
        super(CustomQWebEngine, self).__init__(*args, **kwargs)
        QWebEngineProfile.defaultProfile().setPersistentCookiesPolicy(QWebEngineProfile.NoPersistentCookies)
        QWebEngineProfile.defaultProfile().cookieStore().cookieAdded.connect(self.onCookieAdd)
        QWebEngineProfile.defaultProfile().setHttpUserAgent(
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.122 Safari/537.36"
        )
        self._cookies = []

    def onCookieAdd(self, cookie):
        # Just receive cookie from facebook
        c = QNetworkCookie(cookie)
        # print("cookie added")
        # print(self.get_cookies())
        # print("="*80)
        if re.search(r'facebook.com', c.domain()):
            name = bytearray(c.name()).decode()
            if name not in ["ATN", "IDE", '_js_datr', 'checkpoint']:
                self._cookies.append(c)
                if name == 'fr':
                    fr_cookie_name_timestamp = None
                    try:
                        fr_cookie_name_timestamp = c.expirationDate().toPyDateTime().timestamp()
                    except:
                        fr_cookie_name_timestamp = 1668137438
                    x = datetime.timedelta(days=82, seconds=86341, microseconds=72000)
                    wd_expiry = fr_cookie_name_timestamp - x.total_seconds()
                    # Create wd cookie
                    wd_cookie = QNetworkCookie()
                    wd_cookie.setName(bytes('wd'.encode()))
                    wd_cookie.setPath('/')
                    wd_cookie.setValue(bytes('1076x736'.encode()))
                    wd_cookie.setDomain('.facebook.com')
                    wd_cookie.setExpirationDate(datetime.datetime.fromtimestamp(wd_expiry))
                    wd_cookie.setHttpOnly(False)
                    wd_cookie.setSecure(True)
                    wd_cookie.__setattr__("sameSite", "Lax")
                    self._cookies.append(wd_cookie)

    def setCookies(self, cookies):
        try:
            if cookies and isinstance(cookies, list):
                for cookie in cookies:
                    qnet_cookie = QNetworkCookie()
                    qnet_cookie.setName(bytes(cookie.get('name').encode()))
                    if cookie.get('domain'):
                        qnet_cookie.setDomain(cookie.get('domain'))
                    else:
                        qnet_cookie.setDomain('.facebook.com')
                    
                    qnet_cookie.setValue(bytes(cookie.get('value').encode()))
                    if cookie.get('path'):
                        qnet_cookie.setPath(cookie.get('path'))
                    else:
                        qnet_cookie.setPath("/")
                        
                    if cookie.get('expiry'):
                        expiration_date = QDateTime.fromTime_t(cookie.get('expiry'))
                        qnet_cookie.setExpirationDate(expiration_date)
                    else:
                        expiration_date = QDateTime.fromTime_t(1668137438)
                       
                  
                    if cookie.get('secure'):
                        qnet_cookie.setSecure(cookie.get('secure'))
                    else:
                        qnet_cookie.setSecure(True)
                        
                        
                    if cookie.get('httpOnly'):
                        qnet_cookie.setHttpOnly(cookie.get('httpOnly'))
                    else:
                        qnet_cookie.setHttpOnly(False)
                        
                        
                    QWebEngineProfile.defaultProfile().cookieStore().setCookie(QNetworkCookie(qnet_cookie))
        except Exception as ex:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Thông báo")
            dlg.setText(f"Cookie không hợp lệ!\n {ex}")
            dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            dlg.setIcon(QMessageBox.Information)
            button = dlg.exec()

    def clean_cookies(self):
        print("*"*80)
        clean_cookies, added = [], []
        try:
            # Create list of cookie keys
            names = set()
            for c in self._cookies:
                name = bytearray(c.name()).decode()
                names.add(name)
            print(names)
            # Find max expiry time for each cookie key
            max_per_name = dict()
            for c_key in names:
                max_per_name[f'{c_key}'] = 973999838
            for c_key in names:
                for c in self._cookies:
                    exp = None
                    try:
                        exp = c.expirationDate().toPyDateTime().timestamp()
                    except:
                        exp = 1668137438
                    
                    name = bytearray(c.name()).decode()
                    if c_key == name:
                        if max_per_name[f'{c_key}'] < exp:
                            max_per_name[f'{c_key}'] = exp
                        else:
                            max_per_name[f'{c_key}'] = exp
            print(max_per_name)
            # Keep cookie keys with max one
            for c in self._cookies:
                exp = None
                exp = None
                try:
                    exp = c.expirationDate().toPyDateTime().timestamp()
                except:
                    exp = 1668137438
                    
                # exp = c.expirationDate().toPyDateTime().timestamp()
                name = bytearray(c.name()).decode()
                if max_per_name[f'{name}'] == exp and name not in added:
                    clean_cookies.append(c)
                    added.append(name)
        except KeyError:
            pass
        return clean_cookies

    def get_cookies(self, except_cookies_name: List[str] = None):
        """Get cookies
        Args:
            except_cookies_name (list(str)): list of string cookie name not want to get
        Returns:
            List of cookies
        """
        cookies_list = []
        clean_cookies = self.clean_cookies()
        for c in clean_cookies:
            name = bytearray(c.name()).decode()
            exp = None
            try:
                exp = c.expirationDate().toPyDateTime().timestamp()
            except:
                exp = 1668137438
            
            data = {
                "name": name,
                "domain": c.domain(),
                "value": bytearray(c.value()).decode(),
                "path": c.path(),
                "expiry": exp,
                "secure": c.isSecure(),
                "httpOnly": c.isHttpOnly(),
                "sameSite": "None" if name != 'wd' else 'Lax'
            }
            if except_cookies_name is None:
                cookies_list.append(data)
            elif name not in except_cookies_name:
                cookies_list.append(data)
        return cookies_list


class CustomDialog(QDialog):
    def __init__(self, title, message, reject=None, accept=None):
        super().__init__()
        self.title = title
        self.message = message
        self.setWindowTitle(self.title)

        QBtn = QDialogButtonBox.Cancel
        if accept:
            QBtn = QDialogButtonBox.Ok
        if all([reject, accept]):
            QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.rejected.connect(self.reject)
        self.buttonBox.accepted.connect(self.accept)

        self.layout = QVBoxLayout()
        message = QLabel(self.message)
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


class ImportExportLoginInfo:
    def __init__(self, filename, data: dict = None):
        self.filename = filename
        self.data = data
        self.export = self._export
        self.import_ = self._import

    def _export(self):
        with open(self.filename, 'w') as f:
            import json, base64
            b = bytes(json.dumps(self.data).encode())
            f.write(base64.b85encode(b).decode())
            f.close()

    def _import(self):
        try:
            with open(self.filename, 'r') as f:
                import json, base64
                ct = ""
                for line in f.readlines():
                    ct += line
                ct = ct.strip()
                b = base64.b85decode(bytes(ct.encode()))
                f.close()
                return json.loads(b.decode())
        except Exception:
            return None
    def _import_json(self):
        try:
            data = self._import()
            if data:
                data = data.replace("'",'"')
            return json.loads(data)
        except Exception as ex:
            return None

