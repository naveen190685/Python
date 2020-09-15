from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote import webelement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# See examples at: https://github.com/SergeyPirogov/webdriver_manager/tree/master/tests

class Browser:
    driver = None
    element = None
    myLocator: tuple
    caps = None

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
        if not isinstance(key, tuple):
            key = key.split(":")
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
        else:
            tup = key
        return tup

    def findElement(self, by):
        return self.__find_element(by)

    def __find_element(self, by):
        if isinstance(by, tuple):
            return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by))
        elif isinstance(by, str):
            key = by.split(":")
            if len(key) == 1:
                return self.__getSingleLocator(by)
            elif len(key) == 2:
                return self.__find_element(self.__getDoubleLocator(by))

    def __find_elements(self, by):
        if len(self.driver.find_elements(*by)) > 0:
            return self.driver.find_elements(*by)

    def __getActiveElement(self):
        return self.driver.switch_to.active_element

    # def __setwait(self):
    #     self.wait = WebDriverWait(self.driver, 10)

# PUBLIC FUNCTIONS

    def open_chrome(self):
        from webdriver_manager.chrome import ChromeDriverManager
        # self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        caps = DesiredCapabilities().CHROME
        caps["pageLoadStrategy"] = "normal" # complete
        # caps["pageLoadStrategy"] = "eager"  #  interactive
        # caps["pageLoadStrategy"] = "none"
        self.driver = webdriver.Chrome(desired_capabilities=caps, executable_path="C:/Jenkins/chromedriver.exe")

    def open_firefox(self):
        from webdriver_manager.firefox import GeckoDriverManager
        caps = DesiredCapabilities().FIREFOX
        caps["pageLoadStrategy"] = "normal"  # complete
        # caps["pageLoadStrategy"] = "eager"  #  interactive
        # caps["pageLoadStrategy"] = "none"
        self.driver = webdriver.Firefox(desired_capabilities=caps, executable_path=GeckoDriverManager().localDependency())

    def open_ie(self):
        from webdriver_manager.microsoft import IEDriverManager
        caps = DesiredCapabilities().INTERNETEXPLORER
        caps["pageLoadStrategy"] = "normal"  # complete
        # caps["pageLoadStrategy"] = "eager"  #  interactive
        # caps["pageLoadStrategy"] = "none"
        self.driver = webdriver.Ie(desired_capabilities=caps, executable_path=IEDriverManager().localDependency())

    def open_edge(self):
        from webdriver_manager.microsoft import IEDriverManager
        caps = DesiredCapabilities().EDGE
        caps["pageLoadStrategy"] = "normal"  # complete
        # caps["pageLoadStrategy"] = "eager"  #  interactive
        # caps["pageLoadStrategy"] = "none"
        self.driver = webdriver.Ie(desired_capabilities=caps, executable_path=IEDriverManager().localDependency())

    def goTo(self, url):
        self.driver.get(url)

    def click(self, locator):
        self.__find_element(locator).click()

    def submit(self):
        self.driver.switch_to_active_element().submit()

    def getText(self, locator):
        return self.__find_element(locator).text

    def write(self, content):
        webElement = self.driver.switch_to.active_element
        tagIsInput = webElement.get_attribute("tagName").lower() == "input"
        isElementVisible = webElement.get_attribute("type").lower() != "hidden"
        if tagIsInput and isElementVisible:
            webElement.send_keys(content)
        else:
            self.driver.find_element_by_xpath("//input[@type!='hidden']").send_keys(content)

    def write(self, locator, content):
        self.element = self.__find_element(locator)
        self.element = WebDriverWait(self.driver, 10).until(EC.visibility_of(self.element))
        self.element.send_keys(content)

    def closeBrowser(self):
        self.driver.close()

    def submit(self):
        self.__getActiveElement().submit()

    def waitForVisibleElement(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.__getDoubleLocator(locator)))

    def waitForInvisibleElement(self, locator):
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(self.__getDoubleLocator(locator)))

    def waitForClickable(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.__getDoubleLocator(locator)))
