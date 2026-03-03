from .base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)  # ← И тоже отступы!
