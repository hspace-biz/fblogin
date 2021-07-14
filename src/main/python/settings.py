from pathlib import Path

import os

temp = Path(__file__).parent.parent / 'resources' / 'temp'
if not temp.exists():
    os.mkdir(temp.as_posix())

TNITBEST321JS = Path(__file__).parent.parent / 'resources' / 'temp' / 'TNITBEST321JS.json'

LOGIN_URL = "http://13.212.232.55:2307/login"
