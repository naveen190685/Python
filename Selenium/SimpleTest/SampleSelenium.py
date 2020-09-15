from selenium import webdriver

# See examples at: https://github.com/SergeyPirogov/webdriver_manager/tree/master/tests

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path=ChromeDriverManager().localDependency())


# from webdriver_manager.firefox import GeckoDriverManager
# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

# from webdriver_manager.microsoft import IEDriverManager
# driver = webdriver.Ie(executable_path=IEDriverManager().install())

def find_element(by):
    if len(driver.find_elements(by)) > 0:
        return driver.find_element_by_xpath(by)


def find_elements(by):
    if len(driver.find_elements(by)) > 0:
        return driver.find_elements_by_xpath(by)


def click(by):
    find_element(by).click()


driver.get("https://qaadmin:rMoEW97fk0eLKPulG5s%2Byg%3D%3D@qa.np.bunnings.co.nz")
driver.fullscreen_window()

click("//div[contains(@class,'topLeftIconContainer')]")
level_1_elements = find_elements("//ul[@class = 'level-1']/div/li[@class!='levelBg twoColumn']")
print(len(level_1_elements))

driver.close()
