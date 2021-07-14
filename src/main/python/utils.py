from PyQt5.QtNetwork import QNetworkCookie
from PyQt5.QtWebEngineWidgets import QWebEngineProfile, QWebEngineView
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel


class CustomQWebEngine(QWebEngineView):
    external_windows = []

    def __init__(self, *args, **kwargs):
        super(CustomQWebEngine, self).__init__(*args, **kwargs)
        QWebEngineProfile.defaultProfile().cookieStore().cookieAdded.connect(self.onCookieAdd)
        self._cookies = []

    def onCookieAdd(self, cookie):
        self._cookies.append(QNetworkCookie(cookie))

    def get_cookies(self):
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
                    "httponly": c.isHttpOnly(),
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
