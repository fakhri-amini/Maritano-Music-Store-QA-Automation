import pytest

from selenium import webdriver

from config.config import BROWSER


@pytest.fixture
def driver():

    if BROWSER == "chrome":

        driver = webdriver.Chrome()

    else:

        driver = webdriver.Chrome()

    driver.maximize_window()

    yield driver

    driver.quit()