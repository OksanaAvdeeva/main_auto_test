from pages.main_page import MainPage


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, "http://selenium1py.pythonanywhere.com/")
    page.open()
    page.should_be_login_link()