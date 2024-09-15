import requests

class WeChall:
    def __init__(self):
        self.base_url = "https://www.wechall.net"
        self.cookies = self.handle_cookies()
        self.s = requests.session()

    def handle_cookies(self):
        with open("cookies.txt") as f:
            cookies_raw = f.read().splitlines()

        cookies={}
        for cookie_raw in cookies_raw:
            cookie = cookie_raw.split(":")
            cookies[cookie[0]] = cookie[1]

        return cookies

