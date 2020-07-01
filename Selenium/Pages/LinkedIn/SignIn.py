class SignIn:

    __browser = None

    def __init__(self, browser):
        self.__browser = browser

    __EmailOrPhone = "username"
    __Password = "password"

    def enterEmail(self, mailOrPhone):
        self.__browser.write(self.__EmailOrPhone, mailOrPhone)

    def enterPassword(self, password):
        self.__browser.write(self.__Password, password)