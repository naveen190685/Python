import pytest

from Programs.Selenium.Pages.LinkedIn.LandLinkedIn import Landing
from Programs.Selenium.Pages.LinkedIn.SignIn import SignIn
from Programs.Selenium.core.Core import Browser

I = None

@pytest.fixture()
def browser():
        global I
        if I is None:
            I = Browser()
            I.open_chrome()
            I.goTo("https://www.linkedin.com")
        return I

@pytest.fixture()
def land(browser):
    return Landing(browser)


@pytest.fixture()
def signIn(browser):
    return SignIn(browser)