import time


class JoinNow:

    __browser = None

    def __init__(self, browser):
        self.__browser = browser

    __EmailOrPhone = "email-or-phone"
    __Password = "password"
    __AgreeJoin = "join-form-submit"
    Error = "xpath: //p[@class = 'alert-content']"

    def enterEmail(self, mailOrPhone):
        self.__browser.write(self.__EmailOrPhone, mailOrPhone)

    def enterPassword(self, password):
        self.__browser.write(self.__Password, password)

    def AgreeJoin(self):
        self.__browser.click(self.__AgreeJoin)
        time.sleep(5)

    def checkErrorIs(self, text):
        return self.__browser.getText(self.Error) == text, self.__browser.getText(self.Error)
        # myelement = self.__browser.findElement("error-for-username")
        # print(f' Text found is {myelement.text}')
        # return myelement.text == text
