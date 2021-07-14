import re
from PyQt5.QtCore import QDateTime
from PyQt5.QtNetwork import QNetworkCookie
from PyQt5.QtWebEngineWidgets import QWebEngineProfile, QWebEngineView
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel


class CustomQWebEngine(QWebEngineView):

    def __init__(self, *args, **kwargs):
        super(CustomQWebEngine, self).__init__(*args, **kwargs)
        QWebEngineProfile.defaultProfile().setPersistentCookiesPolicy(QWebEngineProfile.NoPersistentCookies)
        QWebEngineProfile.defaultProfile().cookieStore().cookieAdded.connect(self.onCookieAdd)
        self._cookies = []

    def onCookieAdd(self, cookie):
        # Just receive cookie from facebook
        if re.search(r'facebook.com', QNetworkCookie(cookie).domain()):
            self._cookies.append(QNetworkCookie(cookie))

    def setCookies(self, cookies):
        if cookies and isinstance(cookies, list):
            for cookie in cookies:
                qnet_cookie = QNetworkCookie()
                qnet_cookie.setName(bytes(cookie.get('name').encode()))
                qnet_cookie.setDomain(cookie.get('domain'))
                qnet_cookie.setValue(bytes(cookie.get('value').encode()))
                qnet_cookie.setPath(cookie.get('path'))
                expiration_date = QDateTime.fromTime_t(cookie.get('expiry'))
                qnet_cookie.setExpirationDate(expiration_date)
                qnet_cookie.setSecure(cookie.get('secure'))
                qnet_cookie.setHttpOnly(cookie.get('httpOnly'))
                QWebEngineProfile.defaultProfile().cookieStore().setCookie(QNetworkCookie(qnet_cookie))

    def clean_cookies(self):
        clean_cookies, added = [], []
        try:
            # Create list of cookie keys
            names = set()
            for c in self._cookies:
                name = bytearray(c.name()).decode()
                names.add(name)
            # Find max expiry time for each cookie key
            max_per_name = dict()
            for c_key in names:
                max_per_name[f'{c_key}'] = 0
            for c_key in names:
                for c in self._cookies:
                    exp = c.expirationDate().toTime_t()
                    name = bytearray(c.name()).decode()
                    if c_key == name:
                        if max_per_name[f'{c_key}'] < exp:
                            max_per_name[f'{c_key}'] = exp
            # Keep cookie keys with max one
            for c in self._cookies:
                exp = c.expirationDate().toTime_t()
                name = bytearray(c.name()).decode()
                if max_per_name[f'{name}'] == exp and name not in added:
                    clean_cookies.append(c)
                    added.append(name)
            self._cookies = clean_cookies
        except KeyError:
            pass

    def get_cookies(self):
        self.clean_cookies()
        cookies_list = []
        for c in self._cookies:
            name = bytearray(c.name()).decode()
            if name not in ["ATN", "IDE"]:
                data = {
                    "name": name,
                    "domain": c.domain(),
                    "value": bytearray(c.value()).decode(),
                    "path": c.path(),
                    "expiry": c.expirationDate().toTime_t(),
                    "secure": c.isSecure(),
                    "httpOnly": c.isHttpOnly(),
                    "sameSite": "None"
                }
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
