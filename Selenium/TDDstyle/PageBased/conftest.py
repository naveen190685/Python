import pytest

from Programs.Selenium.Pages.LinkedIn.LinkedInHome import LinkedInHome
from Programs.Selenium.Pages.LinkedIn.LinkedInSignIn import LinkedInSignIn
from Programs.Selenium.Pages.LinkedIn.JoinNow import JoinNow
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
def linkedInHome(browser):
    return LinkedInHome(browser)


@pytest.fixture()
def linkedInSignIn(browser):
    return LinkedInSignIn(browser)


@pytest.fixture()
def joinNow(browser):
    return JoinNow(browser)
