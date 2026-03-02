import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def browser(request):
    print("\nstart chrome browser for test..")
    service = Service(ChromeDriverManager().install())
    _browser = webdriver.Chrome(service=service)
    _browser.maximize_window()
    yield _browser
    _browser.quit()
    print("browser closed")

@pytest.mark.parametrize('language', ["en-gb","ru"])
def test_guest_should_see_login_link(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")