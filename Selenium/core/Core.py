from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote import webelement
from selenium.webdriver.support import expected_conditions


# See examples at: https://github.com/SergeyPirogov/webdriver_manager/tree/master/tests


class Browser:
    driver = None
    element = None
    myLocator: tuple

#PRIVATE FUNCTIONS

    def __getSingleLocator(self, by):
        if len(self.driver.find_elements_by_id(by)) > 0:
            return self.driver.find_element_by_id(by)
        elif len(self.driver.find_elements_by_name(by)) > 0:
            return self.driver.find_element_by_name(by)
        elif len(self.driver.find_elements_by_link_text(by)) > 0:
            return self.driver.find_element_by_link_text(by)

    def __getDoubleLocator(self, key):
        tup: tuple
        key[0] = key[0].lower()  # changing to lowercase
        key[1] = key[1].strip()  # Taking out the spaces on both sides
        if key[0] == "id":
            tup = (By.ID, key[1])
        elif key[0] == "name":
            tup = (By.NAME, key[1])
        elif key[0] == "xpath":
            tup = (By.XPATH, key[1])
        elif key[0] == "linktext":
            tup = (By.LINK_TEXT, key[1])
        elif key[0] == "partiallinktext":
            tup = (By.PARTIAL_LINK_TEXT, key[1])
        return self.__find_element(tup)

    def __find_element(self, by):
        if isinstance(by, tuple):
            if len(self.driver.find_elements(*by)) > 0:
                return self.driver.find_element(*by)
        elif isinstance(by, str):
            key = by.split(":")
            if len(key) == 1:
                return self.__getSingleLocator(by)
            elif len(key) == 2:
                return self.__getDoubleLocator(key)

    def __find_elements(self, by):
        if len(self.driver.find_elements(*by)) > 0:
            return self.driver.find_elements(*by)

    def __getActiveElement(self):
        return self.driver.switch_to.active_element

# PUBLIC FUNCTIONS

    def open_chrome(self):
        from webdriver_manager.chrome import ChromeDriverManager
        # self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(executable_path="C:/Jenkins/chromedriver.exe")

    def open_firefox(self):
        from webdriver_manager.firefox import GeckoDriverManager
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    def open_ie(self):
        from webdriver_manager.microsoft import IEDriverManager
        self.driver = webdriver.Ie(executable_path=IEDriverManager().install())

    def goTo(self, url):
        self.driver.get(url)

    def click(self, locator):
        self.__find_element(locator).click()

    def write(self, content):
        webElement = self.driver.switch_to.active_element
        tagIsInput = webElement.get_attribute("tagName").lower() == "input"
        isElementVisible = webElement.get_attribute("type").lower() != "hidden"
        if tagIsInput and isElementVisible:
            webElement.send_keys(content)
        else:
            self.driver.find_element_by_xpath("//input[@type!='hidden']").send_keys(content)

    def write(self, locator, content):
        self.__find_element(locator).send_keys(content)

    def closeBrowser(self):
        self.driver.close()

    def submit(self):
        self.__getActiveElement().submit()
