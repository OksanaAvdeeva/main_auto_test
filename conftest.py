import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# 🆕 РЕГИСТРИРУЕМ ОПЦИИ!
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: en, ru...")

@pytest.fixture(scope="function")
def browser(request):
    # 🆕 Читаем язык из командной строки!
    user_language = request.config.getoption("language")
    print(f"\nstart chrome browser for test.. (lang: {user_language})")

    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    options.add_argument("--window-size=1920,1080")

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
