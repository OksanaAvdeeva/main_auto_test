class BasePage():
    def __init__(self, browser, url):      # ← 4 пробела!
        self.browser = browser             # ← 8 пробелов!
        self.url = url                     # ← 8 пробелов!

    def open(self):                        # ← 4 пробела!
        self.browser.get(self.url)         # ← 8 пробелов!
