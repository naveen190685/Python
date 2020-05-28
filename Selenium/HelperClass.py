from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.remote import webelement

# See examples at: https://github.com/SergeyPirogov/webdriver_manager/tree/master/tests


class Helper:
    driver = None
    element = None

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

    def find_element(self, by):
        if len(self.driver.find_elements(by)) > 0:
            return self.driver.find_element(by)

    def find_elements(self, by):
        if len(self.driver.find_elements(by)) > 0:
            return self.driver.find_elements(by)

    def click(self, locator):
        if len(locator.split(":")) == 1:
            self.clickWithSingleLocator(locator)
        else:
            self.click(self.getLocator(locator))


    def getLocator(self, locator):
        by = None
        key = locator.split(":")
        if len(key) == 1:
            by = By.id(locator)
        elif len(key) == 2:
            key[0] = key[0].toLowerCase()
            key[1] = key[1].trim()
        if key[0] == "id":
            by = By.id(key[1])
        if key[0] == "name":
            by = By.name(key[1])
        if key[0] == "xpath":
            by = By.xpath(key[1])
        if key[0] == "linktext":
            by = By.linkText(key[1]);
        elif key[0] == "particallinktext":
            by = By.partialLinkText(key[1])
        else:
            print("NO LOCATOR MATCHED")
        return by

    def clickWithSingleLocator(self, locator):
        locatorStore = ""
        try:
            if len(self.driver.find_elements_by_id(locator)) > 0:
                self.driver.find_element_by_id(locator).click()
            if len(self.driver.find_elements_by_name(locator)) > 0:
                self.driver.find_element_by_name(locator).click()
            elif len(self.driver.find_elements_by_link_text(locator)) > 0:
                self.driver.find_element_by_link_text(locator).click()
            elif len(self.driver.find_elements_by_xpath("//*[normalize-space(text())='" + locator + "' and @type!='hidden']")) > 0:
                locatorStore = "//*[normalize-space(text())='" + locator + "' and @type!='hidden']"
                self.driver.find_element_by_xpath(locatorStore).click()
            elif len(self.driver.find_elements_by_xpath("//*[normalize-space(text())='" + locator + "']")) > 0:
                locatorStore = "//*[normalize-space(text())='" + locator + "']"
                self.driver.find_element_by_xpath(locatorStore).click()
            elif len(self.driver.find_elements_by_xpath("//*[normalize-space(@value)='" + locator + "' and @type!='hidden']")) > 0:
                locatorStore = "//*[normalize-space(@value)='" + locator + "']"
                self.driver.find_element_by_xpath(locatorStore).click()
            elif len(self.driver.find_elements_by_xpath("//*[normalize-space(@value)='" + locator + "']")) > 0:
                locatorStore = "//*[normalize-space(@value)='" + locator + "']"
                self.driver.find_element_by_xpath(locatorStore).click()
            else:
                self.driver.find_element_by_id(locator).click()
        except ElementClickInterceptedException:
            locatorStore = locatorStore.replace("]", "]/..")
            self.driver.find_element_by_xpath(locatorStore).click()


    def write(self, content):
        webElement = self.driver.switch_to.active_element
        tagIsInput = webElement.get_attribute("tagName").lower() == "input"
        isElementVisible = webElement.get_attribute("type").lower() != "hidden"
        if tagIsInput and isElementVisible:
            webElement.send_keys(content)
        else:
            self.driver.find_element_by_xpath("//input[@type!='hidden']").send_keys(content)

    def closeBrowser(self):
        self.driver.close()

    def submit(self):
        self.getActiveElement().submit()

    def getActiveElement(self):
        return self.driver.switch_to.active_element