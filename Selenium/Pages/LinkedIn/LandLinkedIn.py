class Landing():
    browser = None
    __SignIn = "linktext: Sign in"
    __Join_Now = "linktext: Join now"


    def __init__(self, browser):
        self.browser = browser

    def SignIn(self):
        self.browser.click(self.__SignIn)

    def Join(self):
        self.browser.click(self, self.__Join_Now)
