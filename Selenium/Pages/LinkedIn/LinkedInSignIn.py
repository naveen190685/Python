class LinkedInSignIn:

    __browser = None

    def __init__(self, browser):
        self.__browser = browser

    __EmailOrPhone = "username"
    __Password = "password"

    def enterEmail(self, mailOrPhone):
        self.__browser.write(self.__EmailOrPhone, mailOrPhone)

    def enterPassword(self, password):
        self.__browser.write(self.__Password, password)

    def submit(self):
        self.__browser.submit()

    def checkErrorIs(self, text):
        return self.__browser.getText("error-for-username") == text, self.__browser.getText("error-for-username")
        # myelement = self.__browser.findElement("error-for-username")
        # print(f' Text found is {myelement.text}')
        # return myelement.text == text
