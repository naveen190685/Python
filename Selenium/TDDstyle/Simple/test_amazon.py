import pytest
from Programs.Selenium.core.Helper import Helper

# @pytest.fixture()
# def createDriver():
#     global I
#     I = Helper()
#     I.open_firefox()
#     return I

@pytest.fixture()
def I():
    browser = Helper()
    browser.open_firefox()
    return browser

@pytest.mark.amazon
# def test_Amazon(createDriver):
def test_Amazon(I):
    I.goTo("https://www.amazon.in")
    I.click("Sign in")
    I.write("naveen190685@gmail.com")
    I.click("Continue")
    I.write("kuchBhiDalu")
    I.submit()
    print("RAN SUCCESSFULLY 'AMAZON")
    I.closeBrowser()
