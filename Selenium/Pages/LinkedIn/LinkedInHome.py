from selenium.webdriver.common.by import By
import time

class LinkedInHome():
    _browser = None
    __SignIn = "linktext: Sign in"
    __Join_Now = "linktext: Join now"
    __EmailOrPhone = (By.ID, "username")

    def __init__(self, browser):
        self._browser = browser

    def SignIn(self):
        self._browser.click(self.__SignIn)
        self._browser.waitForInvisibleElement(self.__SignIn)
        time.sleep(3)

    def Join(self):
        self._browser.click(self.__Join_Now)
        self._browser.waitForInvisibleElement(self.__Join_Now)
        time.sleep(3)
